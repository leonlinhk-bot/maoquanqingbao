#!/usr/bin/env python3
"""Keyword dedupe scan for candidate topics (schema-tolerant)."""
import json

def txt(v):
    if isinstance(v, dict):
        return ' '.join(str(x) for x in v.values())
    return str(v)

d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
items = d['items'] if isinstance(d, dict) else d
kws = ['captive', '專屬自保', 'Moody', '穆迪', 'premium financing', '保費融資', 'PHP2Shell',
       'Gallagher Re', 'BlackRock', '貝萊德', 'reprice', '重新定價', '第三方資本']
for k in kws:
    hits = [i for i in items if k.lower() in (txt(i.get('title')) + ' ' + txt(i.get('summary'))).lower()]
    print(f"\n## {k}: {len(hits)}")
    for h in hits[-4:]:
        print('   ', h['publishedAt'][:10], '|', h.get('sourceKey'), '|', txt(h.get('title'))[:70])
