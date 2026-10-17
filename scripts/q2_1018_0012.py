#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, re
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json', encoding='utf-8'))
items = d['items']
kws = ['亚洲保险论坛', '亚洲保险論壇', 'AIF', 'Donaldson', 'Week in Insurance', '一周', ' insolvenc', 'Lockton', 'Allianz Singapore', '医院现金', '住院现金']
for kw in kws:
    hits = [it for it in items if kw.lower() in (it['title']['sc']+it.get('summary',{}).get('sc','')+it['sourceKey']).lower()]
    print('KW %-18s hits=%d' % (kw, len(hits)))
    for h in hits[:4]:
        print('    ', h['publishedAt'][:16], h['sourceKey'], h['title']['sc'][:70])
print('--- items dated 2026-10-17 or later ---')
for it in items:
    if it['publishedAt'] >= '2026-10-17':
        print(it['publishedAt'], it['sourceKey'], it['title']['sc'][:70])
