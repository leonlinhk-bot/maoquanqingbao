#!/usr/bin/env python3
import json
d = json.load(open('data/live-items.json'))
print('META KEYS:', list(d.keys()))
print(json.dumps(d.get('meta'), ensure_ascii=False, indent=1)[:2500])
for it in d['items'][:2]:
    print('\n=== ITEM ===')
    print(json.dumps(it, ensure_ascii=False, indent=1))
