#!/usr/bin/env python3
"""
条目增强：① 同题聚合（clusterCount / clusterId）② 导语字段（summaryShort）

背景（思维朋友追问的两个未闭合项）：
  · clusterCount：设计上有、i18n 文案有（「源同题」），但代码 0 引用、数据 94.3% = 1
    → 现实后果：头部两源（insuranceasia 201 + insurancebusinessmag 151）常报道同一事件，用户看到重复
  · summary：43–966 字，同一字段装了两样东西（导语 / 长摘要）

做法（低成本、可复现）：
  ① 倒排索引（标题关键词）→ 只比较「共享 ≥2 个关键词」的候选对 → SequenceMatcher 相似度
     阈值 0.62 + 发布日期相差 ≤14 天 → 并查集合并成簇
  ② summaryShort：从 summary 截到句末标点、上限 120 字（不新写内容、只做截取）

用法:
  python3 scripts/enrich-items.py           # dry-run
  python3 scripts/enrich-items.py --apply
"""
import json, re, sys, os, shutil, datetime, collections
from difflib import SequenceMatcher

P = '/Users/leonliang/maoquanqingbao/data/live-items.json'

STOP = set('the and for with from that this will its has have are was were 的 了 與 与 及 和 在 是 為 为 對 对 中 後 後'.split())

WORD_RE = re.compile(r'[A-Za-z][A-Za-z\-]{2,}|[\u4e00-\u9fff]{2,4}')
SENT_END = '。！？；.!?;'


def words(title):
    out = set()
    for w in WORD_RE.findall(title or ''):
        w = w.lower()
        if w not in STOP and len(w) >= 2:
            out.add(w)
    return out


def short_of(s, limit=120):
    s = (s or '').strip()
    if len(s) <= limit:
        return s
    cut = s[:limit]
    for i in range(len(cut) - 1, max(0, limit - 40), -1):
        if cut[i] in SENT_END:
            return cut[:i + 1]
    return cut + '…'


class DSU:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[rb] = ra


def main():
    apply = '--apply' in sys.argv
    d = json.load(open(P, encoding='utf-8'))
    items = d['items']
    n = len(items)

    # ① 同题聚合
    inv = collections.defaultdict(list)
    for i, it in enumerate(items):
        for w in words((it.get('title') or {}).get('sc') or ''):
            inv[w].append(i)

    cand = collections.Counter()
    for w, idxs in inv.items():
        if len(idxs) > 40:            # 过于常见的词（如「保险」）不产生候选对
            continue
        for a in range(len(idxs)):
            for b in range(a + 1, len(idxs)):
                cand[(idxs[a], idxs[b])] += 1

    dsu = DSU(n)
    pairs = 0
    for (i, j), shared in cand.items():
        if shared < 2:
            continue
        ti = (items[i].get('title') or {}).get('sc') or ''
        tj = (items[j].get('title') or {}).get('sc') or ''
        if abs(_days(items[i]) - _days(items[j])) > 14:
            continue
        if SequenceMatcher(None, ti, tj).ratio() >= 0.62:
            dsu.union(i, j)
            pairs += 1

    groups = collections.defaultdict(list)
    for i in range(n):
        groups[dsu.find(i)].append(i)

    multi = {k: v for k, v in groups.items() if len(v) > 1}
    changed = 0
    for it in items:
        if it.get('clusterCount') != 1:
            it['clusterCount'] = 1
    for root, idxs in multi.items():
        m = len(idxs)
        for i in idxs:
            if items[i].get('clusterCount') != m:
                changed += 1
            items[i]['clusterCount'] = m
            items[i]['clusterId'] = f"c{root}"

    # ② 导语字段
    short_n = 0
    for it in items:
        s = (it.get('summary') or {})
        if not isinstance(s, dict):
            continue
        sc, tc = s.get('sc') or '', s.get('tc') or ''
        ss, st = short_of(sc), short_of(tc)
        # 独立字段（不塞进 summary 里）→ 前端可直接 tx(it.summaryShort || it.summary)
        it['summaryShort'] = {'sc': ss, 'tc': st}
        if len(ss) < len(sc):
            short_n += 1

    print("=== 同题聚合 ===")
    print(f"  候选对 {len(cand)} ｜ 判定同题对 {pairs}")
    print(f"  簇（>1 条）：**{len(multi)}** ｜ 涉及条目 {sum(len(v) for v in multi.values())}")
    print(f"  clusterCount 变化：{changed} 条")
    for root, idxs in sorted(multi.items(), key=lambda kv: -len(kv[1]))[:6]:
        print(f"    [{len(idxs)} 条] " + " ｜ ".join(
            ((items[i].get('title') or {}).get('sc') or '')[:34] for i in idxs[:3]))

    print("\n=== 导语字段 summaryShort ===")
    print(f"  生成/更新 {short_n} 条（截到句末、上限 120 字）")

    if apply:
        bak = P + '.bak-enrich-' + datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        shutil.copy(P, bak)
        json.dump(d, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(f"\n✔ 已写回（备份 {os.path.basename(bak)}）")


def _days(it):
    try:
        return datetime.datetime.fromisoformat((it.get('publishedAt') or '').replace('Z', '+00:00')).timestamp() / 86400
    except Exception:
        return 0


if __name__ == '__main__':
    main()
