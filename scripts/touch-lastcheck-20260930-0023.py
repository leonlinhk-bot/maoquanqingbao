#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""回写 14+ 信源检查点：全部置为本次采集时刻 2026-09-30T00:55:00+08:00"""
import json

NOW = '2026-09-30T00:55:00+08:00'
p = '/Users/leonliang/maoquanqingbao/data/last-check.json'
d = json.load(open(p, encoding='utf-8'))
d['lastCheck'] = NOW
n = 0
for k, v in d['sources'].items():
    v['last'] = NOW
    n += 1
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f'已回写 lastCheck={NOW}，信源 {n} 个')
