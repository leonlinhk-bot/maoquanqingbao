import json, collections
d = json.load(open('data/live-items.json'))
print('meta:', json.dumps(d.get('meta', {}), ensure_ascii=False)[:600])
items = d['items']
print('total items:', len(items))
print('--- recent 20 ---')
for it in items[:20]:
    print(it.get('publishedAt'), '|', it.get('sourceKey'), '|', it.get('verifyStatus'), '|', (it.get('title', {}) or {}).get('sc', '')[:60])
print('--- sourceKey counts ---')
c = collections.Counter(i.get('sourceKey') for i in items)
print(c.most_common())
print('--- ids of first 60 ---')
print([i.get('id') for i in items[:60]])
