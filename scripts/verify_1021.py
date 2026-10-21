import json, re
live = json.load(open('data/live-items.json'))
items = json.load(open('data/items.json'))
core = json.load(open('data/core.json'))
print('live', len(live['items']), 'items.json', len(items['items']), 'itemCount', items.get('itemCount'), 'core', len(core['items']))
print('meta.itemCount', live['meta']['itemCount'])
app = open('app.js', encoding='utf-8').read()
m = re.search(r'"itemCount"\s*:\s*(\d+)', app)
print('app.js itemCount', m.group(1) if m else 'n/a')
ids = set(i['id'] for i in live['items'])
print('new ids present in items.json:', all(i['id'] in {x['id'] for x in items['items']} for i in live['items'][:11]))
print('top 5 in items.json:')
for it in items['items'][:5]:
    print('  ', it.get('publishedAt'), '|', it.get('id'))
