#!/usr/bin/env python3
import json
p = 'data/live-items.json'
data = json.load(open(p, encoding='utf-8'))
meta = data['meta']
before = (meta.get('asOf'), meta.get('generatedAt'))
meta['asOf'] = '2026-08-22'
meta['generatedAt'] = '2026-08-22T18:06:00+08:00'
json.dump(data, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print("meta 更新: asOf %s -> %s, generatedAt %s -> %s" % (before[0], meta['asOf'], before[1], meta['generatedAt']))
print("itemCount:", meta.get('itemCount'))
