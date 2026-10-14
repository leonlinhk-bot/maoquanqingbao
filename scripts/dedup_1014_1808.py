#!/usr/bin/env python3
"""Check candidate keywords/urls against existing live-items to avoid duplicates."""
import json, sys

d = json.load(open('data/live-items.json'))
items = d['items']
urls = {}
for it in items:
    u = (it.get('originalUrl') or '').lower()
    t = json.dumps(it.get('title', {}), ensure_ascii=False)
    if u:
        urls[u] = it.get('id')
    urls['TITLE::' + t.lower()] = it.get('id')
blob = json.dumps(items, ensure_ascii=False).lower()

KEYS = [
    'sidecar', '側掛', '侧挂', '渝港', 'chongqing', '金融領袖計劃', 'avoidance of double taxation',
    '雙重課稅', 'manulife', 'moody', 'indonesia', 'hsbc life', 'tata aia', 'picc',
    'shipbuilding', 'mclarens', 'scott yin', 'nathan baran', 'nat res', 'national re',
    'silver bond', '銀色債券', 'gallagher', 'iag', 'nrma', 'marine insurance', 'oil vessel',
    'fatalism', 'supply chain', 'trahan', 'casualty ils', 'apec', 'imf warns',
    'hong kong academy of finance', 'principal', 'molly tea', 'apm',
]
for k in KEYS:
    print(f"{k:28s} -> {blob.count(k.lower())}")
print('\n--- recent ids (top 20) ---')
for it in items[:20]:
    print(it.get('sourceKey'), '|', it.get('publishedAt'), '|', it.get('id'))
