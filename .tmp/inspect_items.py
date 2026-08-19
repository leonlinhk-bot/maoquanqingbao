import json, sys

d = json.load(open('data/live-items.json'))
items = d.get('items', [])
print('total items:', len(items))
print('meta:', json.dumps(d.get('meta', {}), ensure_ascii=False)[:500])
print('---recent 15---')
for it in items[:15]:
    print(it['id'], '|', it.get('sourceKey'), '|', it.get('publishedAt'), '|', it['title']['sc'][:45])
print('---existing keys (last 40)---')
keys = [it.get('sourceKey', '') for it in items]
print(keys[:40])
