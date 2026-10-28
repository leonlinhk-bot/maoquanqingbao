#!/usr/bin/env python3
"""精确 URL 去重：候选 vs 库内 originalUrl。"""
import json, os

D = os.path.expanduser('~/maoquanqingbao/.cache1029_0030')
cands = json.load(open(f'{D}/candidates.json'))
lib = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
have = {}
for i in lib['items']:
    u = (i.get('originalUrl') or '').rstrip('/')
    have[u] = (i['publishedAt'], i['title']['sc'])

picks = {
    'artemis': cands['artemis'][:5],
    'ibm': cands['ibm'][:4],
    'insuranceasia': [c for c in cands['insuranceasia'] if 'in-focus' not in c['url'] and 'exclusive' not in c['url']][:6],
}
for src, lst in picks.items():
    print('=' * 30, src)
    for c in lst:
        u = c['url'].rstrip('/')
        if u in have:
            print('  HAVE ', have[u][0][:16], '|', c['title'][:60])
        else:
            print('  NEW  ', c['title'][:70])
            print('         ', c['url'])
