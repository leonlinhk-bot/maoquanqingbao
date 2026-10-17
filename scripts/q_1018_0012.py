#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json', encoding='utf-8'))
items = d['items']
print('total', len(items))
for it in items[:40]:
    print(it['publishedAt'][:16], '|', it['sourceKey'], '|', it['title']['sc'][:70])
print('---- counts by sourceKey for publishedAt >= 2026-10-15 ----')
from collections import Counter
c = Counter(it['sourceKey'] for it in items if it['publishedAt'] >= '2026-10-15')
print(c)
print('---- items mentioning ART / A.I. framework ----')
for it in items:
    if 'ART' in it['title']['sc'] or 'Artificial' in it['title']['sc'] or 'A.I.' in it['title']['sc']:
        print(it['publishedAt'][:16], it['sourceKey'], it['title']['sc'][:80])
