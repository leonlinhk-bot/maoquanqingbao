#!/usr/bin/env python3
"""Show today's items + insuranceasianews date convention."""
import json
from collections import Counter

d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
items = d['items'] if isinstance(d, dict) else d
today = [i for i in items if i['publishedAt'][:10] == '2026-10-27']
print("today count:", len(today))
for i in today:
    print(i['publishedAt'], '|', i['sourceKey'], '|', i['title']['tc'][:50], '|', i['originalUrl'][:90])

print("\n--- insuranceasianews recent 8 ---")
ian = [i for i in items if i['sourceKey'] in ('insuranceasianews',)]
ian.sort(key=lambda x: x['publishedAt'], reverse=True)
for i in ian[:8]:
    print(i['publishedAt'], '|', i['title']['tc'][:45], '|', i['originalUrl'][:85])
print("ian total:", len(ian))
print("\n--- sourceKey counts today ---", Counter(i['sourceKey'] for i in today))
