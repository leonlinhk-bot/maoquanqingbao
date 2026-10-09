import json
d = json.load(open('data/live-items.json'))
print('keys:', list(d.keys()))
print('meta:', json.dumps(d.get('meta', {}), ensure_ascii=False)[:900])
it = d['items']
print('count:', len(it))
for x in it[:10]:
    print(x.get('id'), '|', x.get('publishedAt'), '|', x.get('sourceKey'), '|', x.get('title', {}).get('sc', '')[:45])
print('--- old tail ---')
for x in it[-3:]:
    print(x.get('id'), x.get('publishedAt'))
