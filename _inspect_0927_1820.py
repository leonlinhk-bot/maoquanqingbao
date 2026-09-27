import json
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
items = d['items']
print('meta:', json.dumps(d.get('meta', {}), ensure_ascii=False))
print('total items:', len(items))
for it in items[:30]:
    t = it['title']
    t = t.get('sc') if isinstance(t, dict) else t
    print(it.get('id'), '|', it.get('publishedAt'), '|', it.get('sourceKey'), '|', t[:70])
print('--- keys of item0 ---')
print(list(items[0].keys()))
print(json.dumps(items[0], ensure_ascii=False)[:1200])
