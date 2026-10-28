import json
d = json.load(open('/Users/leonliang/maoquanqingbao/data/core.json'))
print('keys', list(d.keys()))
print('meta', json.dumps(d.get('meta', {}), ensure_ascii=False)[:300])
its = d['items']
print('items', len(its))
for i in its[:5]:
    print(' first:', i.get('publishedAt'), i.get('id'))
for i in its[-3:]:
    print(' last:', i.get('publishedAt'), i.get('id'))
print('stats', json.dumps(d.get('stats', {}), ensure_ascii=False)[:300])
