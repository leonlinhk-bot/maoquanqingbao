import json, re, datetime
D = '/Users/leonliang/maoquanqingbao/data/_1022_0037'
data = json.load(open(D + '/ian.json'))
print('=== all IAN posts (20) ===')
for it in data:
    t = re.sub(r'<[^>]+>', '', it['title']['rendered'])
    print(it['date'], '|', t[:95])
    print('    ', it['link'])
print('\n=== search live-items for related ===')
live = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))['items']
for kw in ['標題黨', 'Conduct In Focus', '652', 'protected cell', 'PCC', 'Skuld', 'ARPC', 'Aon', 'Acorn']:
    hits = [i for i in live if kw.lower() in (json.dumps(i, ensure_ascii=False)).lower()]
    print(f'{kw}: {len(hits)}')
    for h in hits[:3]:
        print('    ', h['id'], h['publishedAt'][:10], h['title']['sc'][:60])
