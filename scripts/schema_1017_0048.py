#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
items = d['items']
for it in items[:40]:
    if it.get('sourceKey') in ('insurancebusinessmag', 'scmp', 'reinsurancenews', 'insuranceasianews'):
        print(it.get('sourceKey'), '|', it.get('sourceTier'), '|', it.get('score'), '|', it.get('boards'), '|', it.get('themes'))
print('--- one ibm full ---')
for it in items:
    if it.get('sourceKey') == 'insurancebusinessmag':
        print(json.dumps(it, ensure_ascii=False, indent=1)[:2200]); break
print('--- sourceKeys in top 200 ---')
from collections import Counter
print(Counter(it.get('sourceKey') for it in items[:200]).most_common(30))
print('--- boards/themes sample ---')
print(Counter(tuple(it.get('boards', [])) for it in items[:200]).most_common(10))
