#!/usr/bin/env python3
import json
d = json.load(open('data/live-items.json'))
for it in d['items']:
    blob = json.dumps(it, ensure_ascii=False)
    if '側掛' in blob or '侧挂' in blob or 'sidecar' in blob.lower():
        print(it.get('publishedAt'), '|', it.get('sourceKey'), '|', it.get('id'), '|', (it.get('title') or {}).get('tc', '')[:90])

print('\n=== artemis feed-out ===')
fo = json.load(open('data/_feed-out/artemis.json', encoding='utf-8'))
for i in fo['items']:
    print(i.get('published_hkt'), '|', i.get('title'), '|', i.get('link'), '| paywalled:', i.get('paywalled'))
