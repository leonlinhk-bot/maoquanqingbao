import json, collections
d = json.load(open('data/live-items.json'))
print('meta:', json.dumps(d.get('meta', {}), ensure_ascii=False)[:800])
items = d['items']
print('total:', len(items))
print('--- top 12 ---')
for i in items[:12]:
    print(i['publishedAt'], '|', i['sourceKey'], '|', i['title']['sc'][:52])
c = collections.Counter(i['sourceKey'] for i in items[:80])
print('--- recent80 sourceKey counts ---')
print(c.most_common())
print('--- ids of last 40 ---')
print([i['id'] for i in items[:40]])
