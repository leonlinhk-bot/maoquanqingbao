#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, sys
d = json.load(open('data/live-items.json'))
items = d['items']
print('total:', len(items))
print('meta itemCount:', d['meta'].get('itemCount'))
print('--- 最近12条 (id / sourceKey / publishedAt / ingestedAt) ---')
for it in items[:12]:
    print(it['id'], '|', it.get('sourceKey'), '|', it.get('publishedAt'), '|', it.get('ingestedAt'))
print('--- 8/21 之后 ingested 的条数 ---')
n = sum(1 for it in items if (it.get('ingestedAt') or '') >= '2026-08-21')
print(n)
ids = set(it['id'] for it in items)
keys = set(it.get('sourceKey') for it in items)
print('--- sourceKeys 分布 ---')
from collections import Counter
print(Counter(it.get('sourceKey') for it in items).most_common(30))
