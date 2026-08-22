#!/usr/bin/env python3
import json, sys

d = json.load(open('data/live-items.json'))
items = d['items']
print('keys:', list(d.keys()))
print('itemCount meta:', d['meta']['itemCount'], 'actual items:', len(items))
print('generatedAt:', d['meta'].get('generatedAt'))
print('--- first 8 items ---')
for it in items[:8]:
    print(it['id'], '|', it.get('publishedAt'), '|', it.get('sourceKey'), '|', it['title']['sc'][:45])
print('--- last 2 items ---')
for it in items[-2:]:
    print(it['id'], '|', it.get('publishedAt'), '|', it.get('sourceKey'))
