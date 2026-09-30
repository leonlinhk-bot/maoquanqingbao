#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""重复检查 + 现有信源用量统计"""
import json

d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
items = d['items']

KEYS = ['hkma-hkicl', 'hkicl', 'mastercard', 'scam-alert', 'ip-financing', 'monetary-statistics',
        'residential-mortgage', 'exchange-fund', 'international-reserves', 'conduct-in-focus',
        'chubb', 'mylegacy', 'prudential-singapore', 'bidv', 'japan-insurance', 'allianz',
        'pioneer-cat-bond', 'kpmg', 'ai-leaders', 'marsh', 'lotte', 'perils', 'disaster-chasers',
        'redcoin', 'stablecoin', 'ipo', 'wealth-management', 'ill-prepared', 'executives',
        'singapore', 'interest-rate']

print("---- URL 命中（按关键词）----")
seen = set()
for k in KEYS:
    for it in items:
        u = (it.get('originalUrl') or '').lower()
        t = it['title']['sc']
        if k in u or k in t.lower():
            key = it['id']
            if key in seen:
                continue
            seen.add(key)
            print(f"[{k}] {it.get('publishedAt')} | {it.get('sourceKey')} | {t[:80]} | {u[:95]}")
print()
print("---- 信源用量 (全部库) ----")
from collections import Counter, defaultdict
c = Counter(it.get('sourceKey') for it in items)
print(dict(c))
print()
print("---- 各源最近条目时间 ----")
last = {}
for it in items:
    sk = it.get('sourceKey')
    if sk not in last:
        last[sk] = it.get('publishedAt')
for k, v in sorted(last.items(), key=lambda x: str(x[1]), reverse=True):
    print(f"{k:24s} {v}")
