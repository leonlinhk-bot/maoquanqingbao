#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, re
d = json.load(open('data/live-items.json'))
items = d['items']
def find(kw, n=6):
    hits = [it for it in items if kw.lower() in (it['id'] + ' ' + it['title']['sc'] + ' ' + str(it.get('originalUrl',''))).lower()]
    print(f"--- '{kw}': {len(hits)} hits")
    for it in hits[:n]:
        print('  ', it['id'], '|', it.get('sourceKey'), '|', it.get('publishedAt'), '|', it['title']['sc'][:70])
for kw in ['taikoo', 'private-credit', 'offshore-reinsur', 'japanese-life', 'sumitomo', 'hdi', 'scam', 'premium-financing', 'postal', 'hong kong insurance authority', '保监局', 'wcl', 'legislative']:
    find(kw)
