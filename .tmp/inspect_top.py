#!/usr/bin/env python3
"""Inspect top items of live-items.json for cron dedup."""
import json, sys

with open('data/live-items.json') as f:
    d = json.load(f)

items = d['items']
print('total items:', len(items))
print('meta.itemCount:', d['meta'].get('itemCount'))
print('generatedAt:', d['meta'].get('generatedAt'))
print('--- top 40 items ---')
for it in items[:40]:
    print(it['id'], '|', it['sourceKey'], '|', it.get('publishedAt', ''), '|', it['title']['sc'][:60])

print('--- sourceKeys in top 200 ---')
from collections import Counter
c = Counter(it['sourceKey'] for it in items[:200])
for k, v in c.most_common():
    print(k, v)
