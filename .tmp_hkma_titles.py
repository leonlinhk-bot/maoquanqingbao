#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract HKMA release titles + links, check against live-items.json."""
import re, json

html = open('.tmp/hkma.html', encoding='utf-8', errors='replace').read()

# find <a href="...20260826-3/">...title...</a>
items = re.findall(r'<a[^>]+href="(/eng/news-and-media/press-releases/\d{4}/\d{2}/[^"]+)"[^>]*>(.*?)</a>', html, re.S)
seen = {}
for href, txt in items:
    txt = re.sub(r'<[^>]+>', '', txt).strip()
    if href in seen:
        continue
    seen[href] = txt
for href, txt in seen.items():
    m = re.search(r'/(\d{8})-\d+/?', href)
    print(m.group(1) if m else '?', '|', href, '|', txt[:100])

d = json.load(open('data/live-items.json'))
existing = set()
for it in d['items']:
    existing.add(it.get('originalUrl', ''))
print('\n--- in DB check ---')
for href in seen:
    full = 'https://www.hkma.gov.hk' + href
    print(('DB' if full in existing else 'NEW'), '|', href)
