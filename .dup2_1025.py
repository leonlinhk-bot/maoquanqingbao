import json
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
items = d['items']
for t in ['Willis', '韋萊', 'Aon', 'WTW', 'Marsh', '達信', 'rates fell', '費率', '軟市場', 'MPF', '強積金', '罪成', '串謀', '移英', 'flood', '洪水', 'people moves', '人事']:
    hits = [i for i in items if t.lower() in json.dumps(i, ensure_ascii=False).lower()]
    print(f'--- {t}: {len(hits)}')
    for h in hits[:5]:
        print('    ', h['publishedAt'][:10], h['id'][:52], '|', h['title']['sc'][:52])
