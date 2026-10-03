import json
d = json.load(open('data/live-items.json'))
print('items:', len(d['items']))
print('meta:', json.dumps(d.get('meta'), ensure_ascii=False)[:800])
keys = {}
for it in d['items']:
    keys[it['sourceKey']] = keys.get(it['sourceKey'], 0) + 1
print('sourceKeys:', json.dumps(keys, ensure_ascii=False))
for it in d['items'][:15]:
    print(it['id'], '|', it['sourceKey'], '|', it['publishedAt'], '|', it['title']['sc'][:45])
