import json
d = json.load(open('data/live-items.json'))
it = d['items'][1]
for k in ['title', 'summary', 'why', 'source', 'originalUrl', 'id', 'publishedAt']:
    print(k, '=', json.dumps(it.get(k), ensure_ascii=False))
print()
it2 = d['items'][6]
for k in ['id', 'sourceKey', 'sourceTier', 'source', 'publishedAt', 'originalUrl', 'boards', 'themes', 'contentKind']:
    print(k, '=', json.dumps(it2.get(k), ensure_ascii=False))
