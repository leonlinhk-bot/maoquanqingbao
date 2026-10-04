import json
d = json.load(open('data/live-items.json'))
print('meta:', json.dumps(d.get('meta'), ensure_ascii=False))
print('items count:', len(d['items']))
for it in d['items'][:20]:
    print(it.get('publishedAt'), '|', it.get('sourceKey'), '|', it.get('sourceTier'), '|', it['id'], '|', it['title']['sc'][:60])
print('---keys sample---')
for it in d['items'][:20]:
    print(it['id'])
