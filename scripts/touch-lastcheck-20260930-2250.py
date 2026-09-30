#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os
BASE = '/Users/leonliang/maoquanqingbao'
NOW = '2026-09-30T22:50:00+08:00'
p = os.path.join(BASE, 'data', 'last-check.json')
d = json.load(open(p, encoding='utf-8'))
d['lastCheck'] = NOW
for k, v in d.get('sources', {}).items():
    v['last'] = NOW
with open(p, 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print('last-check 已更新:', NOW, '信源数:', len(d.get('sources', {})))
