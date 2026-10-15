#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
items = d['items']
diff = 0
for it in items[:400]:
    sc = (it.get('title') or {}).get('sc', '')
    tc = (it.get('title') or {}).get('tc', '')
    if sc and tc and sc != tc:
        diff += 1
        if diff <= 8:
            print('SC:', sc[:60])
            print('TC:', tc[:60])
            print()
print('items where sc!=tc (of first 400):', diff)
print('sample sc:', (items[0].get('title') or {}).get('sc'))
print('sample tc:', (items[0].get('title') or {}).get('tc'))
print('summary sc:', (items[0].get('summary') or {}).get('sc', '')[:100])
print('summary tc:', (items[0].get('summary') or {}).get('tc', '')[:100])
print('tags:', json.dumps(items[0].get('tags'), ensure_ascii=False)[:200])
print('source:', json.dumps(items[0].get('source'), ensure_ascii=False)[:300])
print('contentRole:', json.dumps(items[0].get('contentRole'), ensure_ascii=False))
