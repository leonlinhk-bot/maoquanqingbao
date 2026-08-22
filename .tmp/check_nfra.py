#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
live = json.load(open('data/live-items.json'))
items = live['items']
for it in items:
    if it.get('sourceKey') == 'nfra':
        print(json.dumps(it, ensure_ascii=False, indent=1))
        break
print("=========== another recent one ===========")
for it in items[:6]:
    print(json.dumps({k: it.get(k) for k in ('id','publishedAt','originalUrl','contentKind','sourceTier','sourceKey','boards','themes')}, ensure_ascii=False))
