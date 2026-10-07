#!/usr/bin/env python3
"""
Feed 通道批量采集（只处理已探测确认「有 feed」的源）。

产出：
  data/_feed-out/<key>.json  每源标准结构（新增条目）
  data/_feed-inbox.json      汇总候选池（供入库流程取用）
  data/_feed-report.md       本次运行摘要（cron 推送用）

定位：把「搜索 + 抓取」改成「订阅」，提升**不漏率**与**时间准确性**。
      脚本只负责「拉取 + 规范化 + 过滤 + 去重」；入库判断（价值/分类/中文摘要）
      仍由采集流程做 —— 本脚本不直接写 live-items.json。

用法: python3 scripts/feed-collect.py [--quiet]
"""
import os, sys, re, json, importlib.util
from datetime import datetime, timezone, timedelta

ROOT = '/Users/leonliang/maoquanqingbao'
HKT = timezone(timedelta(hours=8))

SOURCES = [
    {'key': 'insuranceasianews', 'url': 'https://insuranceasianews.com/country/hong-kong/feed/',
     'label': 'InsuranceAsia News · 香港', 'tier': 'pro', 'note': '港险人事与业务动态'},

    # ⚠️ insuranceasia.com 的 RSS 是残缺的：<title> 填的是文章导语、无 description、
    #    guid 是纯数字。真实标题只在 URL slug 里 → 不能直接用于入库，
    #    定位为「线索源」：只提供 URL + 时间，标题与正文需另行抓取。默认停用。
    {'key': 'insuranceasia', 'url': 'https://insuranceasia.com/rss.xml',
     'label': 'InsuranceAsia（残缺，仅线索）', 'tier': 'pro',
     'note': '⚠️ title 为导语非标题——仅作线索发现，需另行抓取；默认停用',
     'enabled': False},

    {'key': 'artemis', 'url': 'https://artemis.bm/feed/',
     'label': 'Artemis', 'tier': 'research', 'note': 'ILS / 巨灾债券 / 再保险资本市场'},

    {'key': 'vtc-cpe', 'url': 'https://cpe.vtc.edu.hk/rss.xml',
     'label': 'VTC CPE（高峰进修学院）', 'tier': 'official',
     # 实测（2026-10-08）：该 /rss.xml 是**全站通用流**，7 条全为网站 UI 元素
     # （Banner / Vplus 导航 / 占位页），无保险 CPD 内容 → 不适用于情报采集，停用。
     # 若日后要接，需先找到按「保险」课程范畴过滤的 feed 或 list 页。
     'note': '⚠️ 实测为全站通用流（7条全 UI 元素、无保险内容）→ 停用',
     'enabled': False},
]

# 网站 UI 元素（Banner / 导航 / 占位页）不是内容 —— 过滤掉
UI_NOISE = re.compile(r'(banner|subsidy\s*site|^\s*site\s*$|main\s*menu|home\s*page|^untitled)',
                      re.I)


def keep(src, item):
    t = (item.get('title') or '')
    if UI_NOISE.search(t):
        return False
    req = src.get('require_any')
    if req and not any(k.lower() in t.lower() for k in req):
        return False
    return True


def load_fetcher():
    p = os.path.join(ROOT, 'scripts', 'feed-fetch.py')
    spec = importlib.util.spec_from_file_location('feed_fetch', p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main():
    quiet = '--quiet' in sys.argv
    ff = load_fetcher()
    state_dir = os.path.join(ROOT, 'data', '_feed-state')
    out_dir = os.path.join(ROOT, 'data', '_feed-out')
    os.makedirs(state_dir, exist_ok=True)
    os.makedirs(out_dir, exist_ok=True)

    inbox, lines, total_new, total_dropped = [], [], 0, 0
    lines.append(f"# Feed 通道采集 · {datetime.now(HKT).strftime('%Y-%m-%d %H:%M')}（HKT）\n")

    for s in SOURCES:
        if s.get('enabled', True) is False:
            lines.append(f"- ⏸ **{s['label']}**：已停用（{s['note']}）")
            continue
        try:
            items = ff.parse_feed(ff.fetch(s['url']))
        except Exception as e:
            # 网络抖动也会走到这里 —— 不要读成「这个源没有内容」
            lines.append(f"- ✘ **{s['label']}** 拉取失败（可能只是网络抖动，下轮重试）：{str(e)[:70]}")
            continue
        if not items:
            lines.append(f"- ⚠ **{s['label']}** 解析 0 条 —— 先怀疑工具，不要当成「没有内容」")
            continue

        sp = os.path.join(state_dir, f"{s['key']}.json")
        prev = json.load(open(sp, encoding='utf-8')) if os.path.exists(sp) else {}
        seen = set(prev.get('seen_ids', []))
        fresh = [i for i in items if i['id'] not in seen]
        new = [i for i in fresh if keep(s, i)]
        dropped = len(fresh) - len(new)

        fp = 'sha256:' + __import__('hashlib').sha256(
            '|'.join(sorted(i['id'] for i in items)).encode()).hexdigest()[:32]

        for i in new:
            inbox.append({**i, 'source': s['key'], 'source_label': s['label'], 'tier': s['tier']})

        extra = f"，过滤 {dropped} 条 UI/无关项" if dropped else ""
        lines.append(f"- {'✔' if new else '·'} **{s['label']}**：窗口 {len(items)} 条，"
                     f"新增 **{len(new)}**{extra}　（{s['note']}）")
        for i in new[:4]:
            flag = '　[付费墙]' if i['paywalled'] else ''
            lines.append(f"    - {i['published_hkt'][:16] if i['published_hkt'] else '?'}　{i['title'][:70]}{flag}")
        total_new += len(new)
        total_dropped += dropped

        json.dump({'source': s['key'], 'source_label': s['label'], 'fetched_at': datetime.now(HKT).isoformat(),
                   'feed_url': s['url'], 'feed_window': len(items), 'entries_fingerprint': fp,
                   'new_count': len(new), 'filtered_out': dropped, 'items': new},
                  open(os.path.join(out_dir, f"{s['key']}.json"), 'w', encoding='utf-8'),
                  ensure_ascii=False, indent=1)
        json.dump({'seen_ids': sorted(seen | {i['id'] for i in items})[-500:],
                   'last_checked': datetime.now(HKT).isoformat(), 'fingerprint': fp, 'feed_url': s['url']},
                  open(sp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

    json.dump({'generated_at': datetime.now(HKT).isoformat(), 'total_new': total_new,
               'total_filtered': total_dropped, 'items': inbox},
              open(os.path.join(ROOT, 'data', '_feed-inbox.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    lines.append(f"\n**合计新增候选：{total_new} 条**（过滤 {total_dropped} 条）"
                 f" → `data/_feed-inbox.json`（待入库判断）")

    report = os.path.join(ROOT, 'data', '_feed-report.md')
    open(report, 'w', encoding='utf-8').write('\n'.join(lines))
    if not quiet:
        print('\n'.join(lines))


if __name__ == '__main__':
    main()
