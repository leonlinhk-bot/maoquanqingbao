#!/usr/bin/env python3
import json

d = json.load(open('data/live-items.json'))
items = d['items']
# dump all sourceKeys and ids to a reference file
with open('.tmp/existing_keys_0821.txt', 'w') as f:
    for it in items:
        f.write(f"{it.get('sourceKey','')}\t{it['id']}\t{it['title']['sc'][:60]}\n")
print('total existing keys:', len(items))
# print items published on 2026-08-20 or later
for it in items:
    pa = it.get('publishedAt','')
    if isinstance(pa, str) and pa >= '2026-08-20':
        print(it['id'], '|', pa, '|', it.get('sourceKey'), '|', it['title']['sc'][:50])
