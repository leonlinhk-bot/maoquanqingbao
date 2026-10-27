#!/usr/bin/env python3
"""Post-publish verification."""
import json, re

base = '/Users/leonliang/maoquanqingbao/'
live = json.load(open(base + 'data/live-items.json'))
items = live['items']
app = open(base + 'app.js', encoding='utf-8').read()
print("live items:", len(items), "| meta.itemCount:", live['meta']['itemCount'])
for it in items[:3]:
    print(" new:", it['id'], '| in app.js:', it['id'] in app)
    print("      title in app.js:", it['title']['tc'][:18], '->', it['title']['tc'][:18] in app)
core = json.load(open(base + 'data/core.json'))
print("core totalItems:", core['stats']['intelligence']['totalItems'])
print("today items:", sum(1 for i in items if i['publishedAt'][:10] == '2026-10-27'))
# duplicate check on originalUrl
from collections import Counter
c = Counter(i['originalUrl'].rstrip('/') for i in items)
dups = {k: v for k, v in c.items() if v > 1}
print("dup urls:", len(dups))
ids = Counter(i['id'] for i in items)
print("dup ids:", {k: v for k, v in ids.items() if v > 1})
poster = open(base + 'posters/poster-2026-10-27.html', encoding='utf-8').read()
print("poster mtime content len:", len(poster), "| has 21:12 marker:", '10月' in poster)
