#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update all source checkpoints to now."""
import json
from datetime import datetime, timezone, timedelta

now = datetime.now(timezone(timedelta(hours=8)))
now_iso = now.strftime('%Y-%m-%dT%H:%M:%S+08:00')

path = 'data/last-check.json'
d = json.load(open(path, encoding='utf-8'))
d['lastCheck'] = now_iso
for k in d.get('sources', {}):
    d['sources'][k]['last'] = now_iso
with open(path, 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print('last-check updated:', now_iso, '| sources:', len(d['sources']))
