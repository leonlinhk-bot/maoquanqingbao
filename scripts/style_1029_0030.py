#!/usr/bin/env python3
import json
from collections import Counter
lib = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
items = lib['items']
recent = [i for i in items if i['publishedAt'] >= '2026-10-15']
print('recent count', len(recent))
print('sourceKey:', Counter(i.get('sourceKey') for i in recent).most_common())
print()
print('themes recent:', Counter(t for i in recent for t in i.get('themes', [])).most_common(30))
print()
print('boards recent:', Counter(b for i in recent for b in i.get('boards', [])).most_common())
print()
print('lang field:', Counter(i.get('lang') for i in recent).most_common())
print('source.lang:', Counter((i.get('source') or {}).get('lang') for i in recent).most_common())
print('score range:', min(i['score'] for i in recent), max(i['score'] for i in recent))
print()
print('=== last 15 ids ===')
for i in items[:15]:
    print(' ', i['id'], '|', i.get('sourceKey'), '|', i['publishedAt'][:16], '| themes:', i.get('themes'))
