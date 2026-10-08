#!/usr/bin/env python3
"""
字段守卫（Field Guard）—— 把「字段卡」从文档变成可执行的校验与修复。

背景：思维朋友抽查发现「字段没有单一事实来源」：
  · boards 出现 41 个取值（35 个非正式，覆盖 259 条）
  · 术语混用（重疾/危疾、红利实现率/分红实现率）
  · 简体版 13% 条目 sc == tc（未转换）
  · clusterCount 94.3% = 1 且前端 0 引用
  · summary 长度 43–966（同一字段装了两样东西）
本脚本做三件事：**能自动修的修掉、不能修的报出来、都留下痕迹**。

用法:
  python3 scripts/field-guard.py           # dry-run
  python3 scripts/field-guard.py --apply   # 写回 live-items.json
"""
import json, re, sys, os, collections, shutil, datetime
from datetime import datetime as dt, timezone, timedelta

P = '/Users/leonliang/maoquanqingbao/data/live-items.json'
HKT = timezone(timedelta(hours=8))

FORMAL_BOARDS = {'reg', 'product', 'insurer', 'tech', 'market', 'family'}

# 非正式取值 → 要么并入正式板块，要么迁进 themes（它本来就是主题不是板块）
BOARDS_TO_BOARD = {
    'firm': 'insurer', 'company': 'insurer', 'carrier': 'insurer',
    'regulatory': 'reg', 'compliance': 'reg', 'supervision': 'reg',
    'macro': 'market', 'economy': 'market', 'capital': 'market',
    'ai': 'tech', 'insurtech': 'tech', 'digital': 'tech', 'fintech': 'tech',
    'product-design': 'product', 'channel': 'product',
    'family-office': 'family', 'wealth': 'family',
}
BOARDS_TO_THEME = {
    'ils': 'ils', 'cat': 'cat', 'marine': 'marine', 'offshore': 'offshore',
    'cross': 'cross-border', 'intl': 'international', 'reinsurance': 'reinsurance',
    'captive': 'captive', 'esg': 'esg', 'health': 'health', 'tax': 'tax',
}

# 术语表：内地/异体用语 → 港险标准用语
TERMS_SC = {'重疾': '危疾', '红利实现率': '分红实现率', '投保人': '保单持有人'}
TERMS_TC = {'重疾': '危疾', '紅利實現率': '分紅實現率', '投保人': '保單持有人'}

# 繁体特征字——只收「与简体不同形」的字。宁漏勿误：
# 同形字（保、管、例、利、富、健、治…）在简体里也存在，收进来会把简体文本误判成繁体。
TRAD_CHARS = set('險單證監條報價實紅債務處資訊營運規則風財產業醫療覺發機構'
                 '導數專頁樣術總額圓億萬億賺虧蝕點')


def has_trad(s):
    return any(c in TRAD_CHARS for c in (s or ''))


def main():
    apply = '--apply' in sys.argv
    d = json.load(open(P, encoding='utf-8'))
    items = d['items']
    now = dt.now(HKT)

    rep = []
    board_fix = theme_add = term_fix = 0
    board_move = collections.Counter()

    for i in items:
        # ── boards：非正式取值归位（板块或主题）──
        bs = i.get('boards') or []
        if isinstance(bs, list) and bs:
            nb, moved = [], False
            for b in bs:
                if b in FORMAL_BOARDS:
                    nb.append(b)
                elif b in BOARDS_TO_BOARD:
                    tgt = BOARDS_TO_BOARD[b]
                    if tgt not in nb:
                        nb.append(tgt)
                    board_move[f"{b} → {tgt}(板块)"] += 1
                    moved = True
                elif b in BOARDS_TO_THEME:
                    th = BOARDS_TO_THEME[b]
                    if th not in (i.get('themes') or []):
                        i.setdefault('themes', [])
                        i['themes'] = list(i['themes']) + [th]
                    board_move[f"{b} → {th}(主题)"] += 1
                    moved = True
                else:
                    # 未知取值：留在原地并记警告（不静默丢弃）
                    nb.append(b)
                    board_move[f"⚠ 未识别: {b}"] += 1
            if moved:
                board_fix += 1
                if apply:
                    i['boards'] = nb

        # ── 术语：双语言分别替换 ──
        for field in ('title', 'summary', 'why'):
            v = i.get(field)
            if not isinstance(v, dict):
                continue
            for lang, tbl in (('sc', TERMS_SC), ('tc', TERMS_TC)):
                s = v.get(lang)
                if not s:
                    continue
                ns = s
                for bad, good in tbl.items():
                    if bad in ns:
                        ns = ns.replace(bad, good)
                if ns != s:
                    term_fix += 1
                    if apply:
                        v[lang] = ns

    # ── 只报告不改的项 ──
    same = sum(1 for i in items if (i.get('title') or {}).get('sc') == (i.get('title') or {}).get('tc'))
    trad_in_sc = sum(1 for i in items if has_trad((i.get('title') or {}).get('sc')))
    pend = [i for i in items if i.get('verifyStatus') == 'pending']
    stale = []
    for i in pend:
        try:
            p = dt.fromisoformat((i.get('publishedAt') or '').replace('Z', '+00:00'))
            if p.tzinfo is None:
                p = p.replace(tzinfo=HKT)
            age = (now - p.astimezone(HKT)).days
            if age > 90:
                stale.append((age, i.get('id'), i.get('sourceKey')))
        except Exception:
            pass
    stale.sort(reverse=True)
    ccs = collections.Counter(i.get('clusterCount') for i in items)
    lens = sorted(len((i.get('summary') or {}).get('sc') or '') for i in items)

    rep.append("# 字段守卫报告")
    rep.append(f"生成 {now.strftime('%Y-%m-%d %H:%M')}（HKT）｜{'已写回' if apply else 'dry-run'}\n")
    rep.append(f"## 自动修复")
    rep.append(f"- boards 归位：**{board_fix} 条**")
    for k, v in board_move.most_common(14):
        rep.append(f"    - {k}：{v}")
    rep.append(f"- 术语替换：**{term_fix} 处**（重疾→危疾 / 红利实现率→分红实现率 等）")
    rep.append(f"\n## 只报告（需人工/上游决定）")
    rep.append(f"- 简体版 sc == tc（整条未转换）：**{same} 条 = {same/len(items)*100:.1f}%**")
    rep.append(f"- 简体标题含繁体字：**{trad_in_sc} 条 = {trad_in_sc/len(items)*100:.1f}%**")
    rep.append(f"- `pending` 超 90 天未复核：**{len(stale)} 条**" +
               (f"（最久 {stale[0][0]} 天 / id={stale[0][1]}）" if stale else ""))
    rep.append(f"- `clusterCount` 分布：{dict(ccs.most_common(4))}")
    rep.append(f"- `summary` 长度：min={lens[0]} 中位={lens[len(lens)//2]} max={lens[-1]}，<80 字 {sum(1 for x in lens if x < 80)} 条")

    txt = '\n'.join(rep)
    open(os.path.join('/Users/leonliang/maoquanqingbao', 'data', '_field-report.md'), 'w', encoding='utf-8').write(txt)
    print(txt)

    if apply:
        bak = P + '.bak-field-' + dt.now().strftime('%Y%m%d%H%M%S')
        shutil.copy(P, bak)
        meta = d.setdefault('meta', {})
        meta.setdefault('changelog', []).insert(0, {
            "date": dt.now().strftime('%Y-%m-%d'),
            "title": {"sc": "字段守卫上线", "tc": "欄位守衛上線"},
            "items": [f"boards 非正式取值归位 {board_fix} 条（板块或主题）",
                      f"术语替换 {term_fix} 处（重疾→危疾等）",
                      "字段卡建立：boards 封闭枚举 + 兜底告警"],
        })
        json.dump(d, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(f"\n✔ 已写回（备份 {os.path.basename(bak)}）")


if __name__ == '__main__':
    main()
