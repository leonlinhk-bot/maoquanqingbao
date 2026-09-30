#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""回写 data/last-check.json：所有信源最后检查时间 = NOW"""
import json, os

BASE = '/Users/leonliang/maoquanqingbao'
NOW = '2026-09-30T18:08:00+08:00'

path = os.path.join(BASE, 'data', 'last-check.json')
d = json.load(open(path, encoding='utf-8'))
d['lastCheck'] = NOW
n = 0
for k, v in d.get('sources', {}).items():
    v['last'] = NOW
    n += 1
json.dump(d, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
open(path, 'a').write('\n')
print(f'last-check 回写完成: lastCheck={NOW}, 信源数={n}')
