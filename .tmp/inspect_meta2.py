#!/usr/bin/env python3
import json
live = json.load(open('data/live-items.json'))
m = live['meta']
for k in ['asOf','roles','cleanedBy','changelog']:
    print('====', k, '====')
    print(json.dumps(m.get(k), ensure_ascii=False, indent=2)[:1800])
