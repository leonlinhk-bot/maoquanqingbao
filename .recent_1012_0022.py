import json
d=json.load(open('data/live-items.json'))
items=d['items']
rec=[it for it in items if (it.get('publishedAt') or '') >= '2026-10-09']
print('items publishedAt>=2026-10-09:', len(rec))
for it in rec:
    print(it.get('publishedAt'),'|',it.get('sourceKey'),'|',it['id'],'|',it['title']['sc'][:60])
print()
print('=== recent sourceKeys ===')
from collections import Counter
print(Counter(it.get('sourceKey') for it in items[:60]).most_common())
print()
print('=== all urls containing key words ===')
kws=['prudential-life','gibraltar','iag','raci','simon','huanggang','athena','fsa']
for it in items[:200]:
    u=it.get('originalUrl','') or ''
    t=it['title']['sc']
    if any(k in (u+t).lower() for k in ['gibraltar','iag-raci','raci','athena re','fsa suspends']):
        print(it.get('publishedAt'),'|',it['id'],'|',t[:70])
