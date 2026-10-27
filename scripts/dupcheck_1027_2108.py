#!/usr/bin/env python3
"""Check whether dup URLs involve the 3 new items."""
import json
from collections import Counter
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
items = d['items']
c = Counter(i['originalUrl'].rstrip('/') for i in items)
new_urls = {i['originalUrl'].rstrip('/') for i in items[:3]}
print("new urls dup?", {u: c[u] for u in new_urls})
dup = [(k, v) for k, v in c.items() if v > 1]
print("total dup urls:", len(dup))
for k, v in dup[:6]:
    ents = [i for i in items if i['originalUrl'].rstrip('/') == k]
    print(f"  {v}x | {ents[0]['sourceKey']} | {ents[0]['title']['tc'][:40]} | {ents[0]['publishedAt'][:10]}")
