import json
d = json.load(open('data/live-items.json'))
it = d['items']
ids = set(x['id'] for x in it)
print('total', len(it))
recent = [x for x in it if str(x.get('publishedAt', ''))[:10] >= '2026-10-07']
recent.sort(key=lambda x: str(x.get('publishedAt')))
print('recent >=10-07:', len(recent))
for x in recent:
    print(x.get('publishedAt'), '|', x.get('sourceKey'), '|', x['id'])
