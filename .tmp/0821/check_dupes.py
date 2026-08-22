import json
from collections import Counter

d = json.load(open('data/live-items.json'))
items = d['items']

print('=== dup check for candidates ===')
keys = ['ping', 'etf', 'taikoo', 'sumitomo', 'hdi', 'oona', 'allianz', 'broker access', 'private credit', 'healthcare plan']
for it in items:
    blob = (it['id'] + ' ' + it['title']['sc']).lower()
    for k in keys:
        if k in blob:
            print(f"  MATCH [{k}]: {it['id']} | {it.get('publishedAt')} | {it['title']['sc'][:60]}")
            break

print()
print('=== sourceKey full list (all) ===')
cks = Counter(it.get('sourceKey', '') for it in items)
for k, v in sorted(cks.items(), key=lambda x: -x[1]):
    print(f'  {k}: {v}')

print()
print('=== latest 3 items per key source ===')
for sk in ['nfra', 'scmp', 'manulife', 'axa', 'prudential', 'aia', 'sunlife', 'fsdc', 'govhk', 'insuranceasia', 'insurancebusinessmag']:
    sub = [it for it in items if it.get('sourceKey') == sk]
    sub.sort(key=lambda x: x.get('publishedAt', ''), reverse=True)
    if sub:
        print(f'  {sk} (latest {sub[0].get("publishedAt")}): {sub[0]["title"]["sc"][:55]}')
