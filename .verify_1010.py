import json, re
live = json.load(open('data/live-items.json'))
items = json.load(open('data/items.json'))
core = json.load(open('data/core.json'))
print('live items:', len(live['items']), 'meta itemCount:', live['meta'].get('itemCount'), 'windowNote:', live['meta']['windowNote']['sc'])
print('items.json itemCount:', items.get('itemCount'), 'len:', len(items['items']))
print('core.json itemCount:', core.get('itemCount'), 'len:', len(core['items']))
app = open('app.js', encoding='utf-8').read()
m = re.search(r'HKII_VER\s*=\s*[^;]+', app)
print('app.js ver:', m.group(0) if m else 'NOT FOUND')
print('app.js id count:', len(re.findall(r'"id":"', app)))
m2 = re.search(r'window\.HKII_VER[^;]*', app)
print('window ver line:', m2.group(0)[:120] if m2 else 'n/a')
# cluster check
cl = [it for it in live['items'] if it.get('clusterCount', 1) > 1][:6]
for it in cl:
    print('cluster', it['clusterCount'], it['id'], '|', it['title']['sc'][:34])
