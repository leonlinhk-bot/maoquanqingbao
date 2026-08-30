#!/usr/bin/env python3
"""Inspect live-items.json meta and recent items."""
import json, sys

with open('data/live-items.json', encoding='utf-8') as f:
    d = json.load(f)

print('meta:', json.dumps(d.get('meta'), ensure_ascii=False))
items = d['items']
print('total items:', len(items))
for it in items[:5]:
    print(json.dumps({k: it.get(k) for k in ('id', 'sourceKey', 'publishedAt', 'title')}, ensure_ascii=False))

# print last-check source list for reference
try:
    lc = json.load(open('data/last-check.json', encoding='utf-8'))
    print('lastCheck:', lc.get('lastCheck'))
    print('sources:', list(lc.get('sources', {}).keys()))
except Exception as e:
    print('last-check read error:', e)
