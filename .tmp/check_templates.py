#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
live = json.load(open('data/live-items.json'))
items = live['items']
print("=== nfra / toutiao / aastocks sample entries ===")
for it in items:
    sk = it.get('sourceKey', '')
    if sk in ('nfra', 'toutiao', 'aastocks', 'hkma_press', 'insuranceasia', 'hket', 'etnet'):
        print(json.dumps(it, ensure_ascii=False, indent=1)[:1200])
        print("---")
        break
# show all distinct sourceKeys
keys = {}
for it in items:
    keys[it.get('sourceKey','')] = keys.get(it.get('sourceKey',''), 0) + 1
print("sourceKey counts:", dict(sorted(keys.items(), key=lambda x: -x[1])[:40]))
