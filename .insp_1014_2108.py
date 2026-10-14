import json
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
print('items:', len(d['items']))
print('meta:', json.dumps(d.get('meta', {}), ensure_ascii=False)[:800])
print('--- top 12 ---')
for it in d['items'][:12]:
    t = (it.get('title') or {})
    print(it.get('id'), '|', it.get('publishedAt'), '|', it.get('sourceKey'), '|', str(t.get('sc'))[:50])
print('--- keys of first item ---')
print(json.dumps(d['items'][0], ensure_ascii=False)[:1200])
