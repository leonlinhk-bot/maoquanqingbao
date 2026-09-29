import json
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
items = d['items']
print('TOPKEYS:', list(d.keys()))
print('meta:', json.dumps(d.get('meta', {}), ensure_ascii=False))
print('total items:', len(items))
for it in items[:25]:
    t = it['title']
    t = t.get('sc') if isinstance(t, dict) else t
    print(it.get('id'), '|', it.get('publishedAt'), '|', it.get('sourceKey'), '|', t[:70])
print('--- item0 keys ---')
print(list(items[0].keys()))
print(json.dumps(items[0], ensure_ascii=False)[:1500])
