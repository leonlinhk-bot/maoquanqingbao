import json

with open('data/live-items.json') as f:
    d = json.load(f)
print('meta:', json.dumps(d.get('meta', {}), ensure_ascii=False))
items = d.get('items', [])
print('total items:', len(items))
for it in items[:8]:
    print('-', it.get('id'), '|', it.get('publishedAt'), '|', it.get('sourceKey'), '|', it.get('title', {}).get('sc'))
