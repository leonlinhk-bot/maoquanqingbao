#!/usr/bin/env python3
"""Dump 2 full sample items + meta shape."""
import json
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
print("top keys:", list(d.keys()))
print("meta.itemCount:", d['meta'].get('itemCount'), "asOf:", d['meta'].get('asOf'), "generatedAt:", d['meta'].get('generatedAt'))
items = d['items']
for i in items[:2]:
    print(json.dumps(i, ensure_ascii=False, indent=1))
print("\n--- last ian item ---")
ian = [x for x in items if x['sourceKey'] == 'insuranceasianews']
print(json.dumps(ian[0], ensure_ascii=False, indent=1))
