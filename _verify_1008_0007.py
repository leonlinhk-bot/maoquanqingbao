import json, re
live=json.load(open('data/live-items.json'))
print('live items:', len(live['items']), 'meta.itemCount:', live['meta']['itemCount'], 'generatedAt:', live['meta']['generatedAt'])
items=json.load(open('data/items.json'))
print('items.json:', items['itemCount'], len(items['items']))
core=json.load(open('data/core.json'))
print('core.json first screen:', len(core['items']), 'full:', core.get('__fullCount'))
app=open('app.js',encoding='utf-8').read()
m=re.search(r'"itemCount":\s*(\d+)', app)
print('app.js itemCount match:', m.group(1) if m else None)
# count ids in app.js DATA
ids=re.findall(r'"id":"([a-z0-9\-]+)"', app)
print('app.js ids:', len(ids))
print('newest 5 in live:')
for it in live['items'][:5]:
    print('  ', it['publishedAt'], it['id'])
