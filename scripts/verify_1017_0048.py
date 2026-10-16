#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
print('meta.itemCount', d['meta']['itemCount'], 'len(items)', len(d['items']), 'generatedAt', d['meta']['generatedAt'])
print('windowNote', json.dumps(d['meta']['windowNote'], ensure_ascii=False))
live = json.load(open('/tmp/hkii_items3.json'))
print('SITE items', len(live['items']), 'site generatedAt', live['meta'].get('generatedAt'))
ids = {it['id'] for it in live['items'][:20]}
print('new in site head:', sorted(x for x in ids if '20261016' in x or '20261017' in x)[:12])
print('--- spot check ---')
for it in d['items'][:3]:
    print(it['id'], '|', it['publishedAt'], '|', it['sourceKey'], '|', it['sourceTier'], it['score'])
    print('   T:', it['title']['sc'])
    print('   S:', it['summary']['sc'][:110])
    print('   W:', it['why']['sc'][:80])
lc = json.load(open('/Users/leonliang/maoquanqingbao/data/last-check.json'))
print('sources all touched:', {v['last'] for v in lc['sources'].values()})
