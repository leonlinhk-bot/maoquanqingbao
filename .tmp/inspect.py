import json

with open('data/live-items.json') as f:
    d = json.load(f)
print('keys:', list(d.keys()))
print('meta:', json.dumps(d.get('meta', {}), ensure_ascii=False))
items = d['items']
print('total items:', len(items))
for it in items[:6]:
    print(it['id'], '|', it.get('sourceKey'), '|', it.get('publishedAt'), '|', it['title']['sc'][:50])
print('--- last 3 ---')
for it in items[-3:]:
    print(it['id'], '|', it.get('sourceKey'), '|', it.get('publishedAt'))
