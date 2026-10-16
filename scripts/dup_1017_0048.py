#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, re
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
items = d['items']
KW = ['Syndicate 2031', 'Red Bridge', 'Generali', 'Isaias', 'SafePoint', 'Nature Coast', 'Allstate',
      '777', 'Wander', 'Gallagher', 'Nepal', 'Credeq', 'VisionFund', 'Global Parametrics', 'Stand ',
      'Travelers', 'Baden-Baden', 'Coalition', 'poaching', 'Marsh', 'mental health', 'AXA survey',
      'HKEX', 'T+1', 'Moody', 'Lloyd']
for k in KW:
    hits = []
    for it in items[:60]:
        blob = json.dumps(it, ensure_ascii=False)
        if k.lower() in blob.lower():
            hits.append((it.get('id'), it.get('publishedAt')))
    print(k, '->', hits[:6])
# recent ids by date
from collections import Counter
c = Counter(it.get('id', '')[-8:] for it in items[:60])
print('recent id tail counts:', c.most_common(6))
print('--- sample full item ---')
print(json.dumps(items[3], ensure_ascii=False, indent=1)[:2600])
