#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dump recent items + sourceKey coverage for dedup reference."""
import json, collections

d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json', encoding='utf-8'))
items = d['items']
print('TOTAL', len(items))
print('meta', json.dumps(d.get('meta', {}), ensure_ascii=False)[:800])
print('--- items sorted by publishedAt desc (top 45) ---')
s = sorted(items, key=lambda x: x.get('publishedAt') or '', reverse=True)
for it in s[:45]:
    print(it.get('publishedAt'), '|', it.get('sourceKey'), '|', it.get('sourceTier'), '|', it.get('id'))
print('--- sourceKey counts ---')
c = collections.Counter(it.get('sourceKey') for it in items)
for k, v in c.most_common():
    print(f'{k}: {v}')
print('--- items published 2026-10-08 ---')
for it in s:
    if (it.get('publishedAt') or '').startswith('2026-10-08'):
        print(it.get('publishedAt'), '|', it.get('id'))
