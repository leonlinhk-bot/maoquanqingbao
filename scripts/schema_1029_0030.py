#!/usr/bin/env python3
import json
from collections import Counter
lib = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
items = lib['items']
print('=== SAMPLE ITEM (latest artemis) ===')
for i in items:
    if i.get('sourceKey') == 'artemis':
        print(json.dumps(i, ensure_ascii=False, indent=1))
        break
print()
print('=== SAMPLE ITEM (latest ibm) ===')
for i in items:
    if i.get('sourceKey') == 'ibm':
        print(json.dumps(i, ensure_ascii=False, indent=1))
        break
print()
print('=== boards distribution ===')
print(Counter(b for i in items for b in i.get('boards', [])))
print('=== sourceTier ===')
print(Counter(i.get('sourceTier') for i in items))
print('=== contentKind ===')
print(Counter(i.get('contentKind') for i in items))
print('=== verifyStatus ===')
print(Counter(i.get('verifyStatus') for i in items))
print('=== themes top 40 ===')
print(Counter(t for i in items for t in i.get('themes', [])).most_common(40))
print('=== sourceKey top ===')
print(Counter(i.get('sourceKey') for i in items).most_common(25))
