#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os
BASE = '/Users/leonliang/maoquanqingbao'
NOW = '2026-10-01T00:55:00+08:00'
p = os.path.join(BASE, 'data', 'last-check.json')
d = json.load(open(p, encoding='utf-8'))
n = 0
for k, v in d.get('sources', {}).items():
    v['last'] = NOW
    n += 1
d['lastCheck'] = NOW
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f'已回写 {n} 个信源；lastCheck = {d["lastCheck"]}')
