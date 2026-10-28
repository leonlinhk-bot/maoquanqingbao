#!/usr/bin/env python3
import json
lib = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
ia = [i for i in lib['items'] if i.get('sourceKey', '').startswith(('ia', 'hkfi', 'nfra', 'aia', 'pru', 'manulife', 'axa', 'sunlife', 'fstb', 'govhk'))]
ia.sort(key=lambda x: x['publishedAt'], reverse=True)
print('regulator/insurer items:', len(ia))
seen = {}
for i in ia:
    k = i.get('sourceKey')
    if k in seen:
        continue
    seen[k] = 1
    print(i['publishedAt'][:16], '|', k, '|', i['title']['sc'][:55], '|', i.get('originalUrl', '')[:100])
print()
print('=== ia* all recent 6 ===')
for i in [x for x in ia if x.get('sourceKey', '').startswith('ia')][:6]:
    print(i['publishedAt'][:16], '|', i.get('sourceKey'), '|', i['title']['sc'][:60])
    print('   ', i.get('originalUrl', ''))
