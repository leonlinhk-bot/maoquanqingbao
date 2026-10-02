import json, collections
d = json.load(open('data/live-items.json'))
print('keys:', list(d.keys()))
print('meta:', json.dumps(d.get('meta', {}), ensure_ascii=False)[:600])
items = d['items']
print('count:', len(items))
print('--- top 12 ---')
for it in items[:12]:
    print(it['id'], '|', it.get('publishedAt'), '|', it.get('sourceKey'), '|', it['title']['sc'][:56])
print('--- per sourceKey counts ---')
c = collections.Counter(i.get('sourceKey') for i in items)
print(dict(c))
