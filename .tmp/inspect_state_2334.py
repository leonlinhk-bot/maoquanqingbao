import json

with open('data/live-items.json') as f:
    d = json.load(f)

print('meta:', json.dumps(d.get('meta', {}), ensure_ascii=False))
items = d.get('items', [])
print('items count:', len(items))
print('--- top 10 items ---')
for it in items[:10]:
    print(it['id'], '|', it.get('sourceKey'), '|', it.get('publishedAt'), '|', it.get('title', {}).get('sc', '')[:40])

print('--- keys of all items (sourceKey) ---')
keys = {}
for it in items:
    k = it.get('sourceKey', '')
    keys[k] = keys.get(k, 0) + 1
print(len(keys), 'unique sourceKeys')

print('--- items with publishedAt >= 2026-08-20 ---')
n = 0
for it in items:
    pa = it.get('publishedAt', '')
    if pa >= '2026-08-20':
        n += 1
        print(it['id'], '|', it.get('sourceKey'), '|', pa, '|', it.get('title', {}).get('sc', '')[:50])
print('count >= 08-20:', n)
