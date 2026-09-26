#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update data/last-check.json: set all source timestamps + lastCheck to now."""
import json, os
BASE = '/Users/leonliang/maoquanqingbao'
NOW = '2026-09-27T01:10:00+08:00'
p = os.path.join(BASE, 'data/last-check.json')
d = json.load(open(p, encoding='utf-8'))
d['lastCheck'] = NOW
for k, v in d.get('sources', {}).items():
    v['last'] = NOW
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('lastCheck ->', d['lastCheck'], '| sources updated:', len(d.get('sources', {})))
