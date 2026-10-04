import json
d = json.load(open('data/live-items.json'))
ids = [it['id'] for it in d['items']]
for k in ['yield', 'crs', 'tax', 'gmt8', 'chan-pui', 'chan', 'fsa', 'japan-fsa', 'prulife', 'pru-life',
          'specified-risk', 'mcv', 'mainland-residents', 'overseas-insurance']:
    hits = [i for i in ids if k in i.lower()]
    print(f'[{k}] {len(hits)}: {hits[:10]}')
# also check the last 40 items' publishedAt to know exact coverage window
last = sorted(d['items'], key=lambda x: x.get('publishedAt', ''), reverse=True)[:25]
print('--- latest 25 by publishedAt ---')
for it in last:
    print(it.get('publishedAt'), '|', it['id'])
