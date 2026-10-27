#!/usr/bin/env python3
"""List 2026-10-25..27 items to spot premium-financing coverage gaps."""
import json
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
items = d['items'] if isinstance(d, dict) else d

def txt(v):
    return ' '.join(str(x) for x in v.values()) if isinstance(v, dict) else str(v)

for day in ('2026-10-25', '2026-10-26', '2026-10-27'):
    sel = [i for i in items if i['publishedAt'][:10] == day]
    print(f"\n### {day}  ({len(sel)})")
    for i in sel:
        print('  ', i['publishedAt'][11:16], i.get('sourceKey'), '|', txt(i.get('title'))[:80])
print("\n--- items mentioning 融資/leverage in Oct ---")
for i in items:
    if i['publishedAt'][:7] == '2026-10' and any(k in txt(i.get('title')) + txt(i.get('summary')) for k in ['保費融資', '保费融资', 'premium financing', '槓桿', '杠杆']):
        print('  ', i['publishedAt'][:10], i.get('sourceKey'), '|', txt(i.get('title'))[:90])
