import json
d = json.load(open('data/live-items.json'))
print('meta:', json.dumps(d.get('meta', {}), ensure_ascii=False))
items = d.get('items', [])
print('item count:', len(items))
for it in items[:6]:
    print(json.dumps({k: it.get(k) for k in ['id', 'sourceKey', 'title', 'publishedAt', 'source', 'contentKind']}, ensure_ascii=False))
print('--- last 3 ---')
for it in items[-3:]:
    print(json.dumps({k: it.get(k) for k in ['id', 'sourceKey', 'publishedAt']}, ensure_ascii=False))
