import json

d = json.load(open('data/live-items.json'))
print('meta:', json.dumps(d.get('meta', {}), ensure_ascii=False))
items = d.get('items', [])
print('items count:', len(items))
for it in items[:10]:
    print(it['id'], '|', it.get('sourceKey'), '|', it['publishedAt'], '|', it['title']['sc'][:40])
