#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, re, collections
D = '/Users/leonliang/maoquanqingbao/data/_1016_0029/'
j = json.load(open(D + 'ian.out', encoding='utf-8'))
for p in j[:4]:
    print(p.get('date'), '|', p.get('date_gmt'), '|', re.sub(r'<[^>]+>', '', p.get('title', {}).get('rendered', ''))[:80])
    print('   ', p.get('link'))

d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
items = d['items'][:120]
print('\n--- recent boards usage ---')
c = collections.Counter()
for it in items:
    c[tuple(it.get('boards', []))] += 1
for k, v in c.most_common(12):
    print(v, list(k))
print('\n--- recent themes sample ---')
for it in items[:6]:
    print(it.get('sourceKey'), '|', it.get('boards'), '|', it.get('themes'), '|', it.get('contentKind'))
print('\n--- rolesImpact sample ---')
for it in items[:4]:
    print(it.get('rolesImpact'), it.get('actions'))
print('\n--- verifyStatus / score spread recent ---')
print(collections.Counter([it.get('verifyStatus') for it in items]).most_common())
print(collections.Counter([it.get('score') for it in items]).most_common(10))
