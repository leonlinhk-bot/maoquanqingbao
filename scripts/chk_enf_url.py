import json
d = json.load(open('data/live-items.json'))
for it in d['items']:
    t = it.get('title', {}).get('sc', '')
    u = it.get('originalUrl', '')
    if 'enforcement' in u or ('纪律' in t and ('罚' in t or '停牌' in t or '处分' in t)):
        print(it.get('publishedAt'), '|', u, '|', t[:70])
