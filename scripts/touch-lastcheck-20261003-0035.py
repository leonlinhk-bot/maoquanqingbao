#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-03 00:35 采集完成后回写 data/last-check.json 各信源时间戳。"""
import json, os

BASE = '/Users/leonliang/maoquanqingbao'
NOW = '2026-10-03T00:35:00+08:00'
path = os.path.join(BASE, 'data', 'last-check.json')
d = json.load(open(path, encoding='utf-8'))
d['lastCheck'] = NOW
for k, v in d.get('sources', {}).items():
    v['last'] = NOW
with open(path, 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print('last-check.json 已更新：', len(d.get('sources', {})), '个信源 ->', NOW)
