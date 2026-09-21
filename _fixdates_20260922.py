# -*- coding: utf-8 -*-
"""修正 future-dated guard 提示：date-only 的 2026-09-22 在 UTC 视角被视为未来。
改为精确到分钟（该文于 09-21 21:15 后、09-22 00:45 抓取之间上线）。"""
import json, os
BASE = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(BASE, 'data', 'live-items.json')
d = json.load(open(p, encoding='utf-8'))
n = 0
for it in d['items']:
    if it.get('id') == 'ibm-japan-typhoon-dujuan-soft-market-test-20260922':
        it['publishedAt'] = '2026-09-22T00:20:00+08:00'
        n += 1
d['meta']['generatedAt'] = '2026-09-22T01:10:00+08:00'
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
chk = json.load(open(os.path.join(BASE, 'data', 'last-check.json'), encoding='utf-8'))
chk['lastCheck'] = '2026-09-22T01:10:00+08:00'
for v in chk.get('sources', {}).values():
    v['last'] = '2026-09-22T01:10:00+08:00'
json.dump(chk, open(os.path.join(BASE, 'data', 'last-check.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('fixed', n)
