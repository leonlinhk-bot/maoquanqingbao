#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, re
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
items = d['items']
KEYS = ['betterme', 'greensill', 'sidecar', 'stand-hires', 'nephila', 'artex-capital',
        'brit-re', 'aces-specialty', 'acic', 'antares', 'meera', 'marsh-revenue',
        'revenue-rises-8', '593667', 'systemic-cyber', 'doyle']
print('--- dup scan by keyword ---')
for k in KEYS:
    hit = [it['id'] for it in items if k.lower() in json.dumps(it, ensure_ascii=False).lower()]
    print('%-16s %d  %s' % (k, len(hit), hit[:3]))
print()
print('--- existing appointment-type items (sample) ---')
n = 0
for it in items:
    t = (it.get('title') or {}).get('sc', '')
    if re.search(r'任命|委任|出任|接任|升任|appoint', t):
        n += 1
        if n <= 12:
            print(' ', it.get('publishedAt'), '|', it.get('sourceKey'), '|', t[:70])
print('total appointment items:', n)
print()
print('--- items with sourceKey reinsurancenews ---')
for it in items:
    if it.get('sourceKey') == 'reinsurancenews':
        print(' ', it.get('publishedAt'), '|', it.get('id'), '|', (it.get('title') or {}).get('sc', '')[:70])
print()
print('--- existing ids starting with artemis- 20261015 ---')
for it in items:
    if it.get('id', '').endswith('20261015') or '20261015' in it.get('id', ''):
        print(' ', it.get('publishedAt'), '|', it.get('sourceKey'), '|', it.get('id'))
