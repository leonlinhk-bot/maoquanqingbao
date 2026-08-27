import json

d = json.load(open('data/live-items.json'))
items = d['items']
print('total items:', len(items))
print('meta:', json.dumps(d.get('meta', {}), ensure_ascii=False))
print('--- recent 12 ---')
for it in items[:12]:
    print(it['id'], '|', it['publishedAt'], '|', it.get('sourceKey', ''), '|', it['title']['sc'][:45])
print('--- sourceKeys (last 40) ---')
keys = [it.get('sourceKey', '') for it in items[:40]]
print(keys)
