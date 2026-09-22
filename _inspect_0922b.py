import json, collections
d=json.load(open('data/live-items.json'))
items=d['items']
print('total',len(items))
print('meta.generatedAt',d['meta'].get('generatedAt'),'itemCount',d['meta'].get('itemCount'))
for it in items[:40]:
    print(it.get('publishedAt'),'|',it.get('sourceKey'),'|',it['id'],'|',it['title']['sc'][:50])
print('---sourceKey counts of top 60---')
c=collections.Counter(it.get('sourceKey') for it in items[:60])
print(c)
