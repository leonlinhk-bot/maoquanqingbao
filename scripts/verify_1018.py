import json
live = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
items = json.load(open('/Users/leonliang/maoquanqingbao/data/items.json'))
core = json.load(open('/Users/leonliang/maoquanqingbao/data/core.json'))
print('live', len(live['items']), 'items', len(items['items']), items.get('itemCount'), 'core', len(core['items']))
print('meta', live['meta']['itemCount'], live['meta']['generatedAt'])
ids = [it['id'] for it in items['items'][:6]]
print(ids)
