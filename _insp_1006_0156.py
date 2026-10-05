import json, collections, datetime
d = json.load(open('data/live-items.json'))
print('keys', list(d.keys()))
print('meta', json.dumps(d.get('meta', {}), ensure_ascii=False)[:1500])
it = d['items']
print('total items', len(it))
print('--- first 12 ---')
for x in it[:12]:
    print(x.get('id'), '|', x.get('publishedAt'), '|', x.get('sourceKey'), '|', (x.get('title') or {}).get('sc', '')[:44])
print('--- recent publishedAt dates ---')
c = collections.Counter((x.get('publishedAt') or '')[:10] for x in it)
for k in sorted(c, reverse=True)[:14]:
    print(k, c[k])
print('--- sourceKey counts (top 30) ---')
c2 = collections.Counter(x.get('sourceKey') for x in it)
for k, v in c2.most_common(30):
    print(k, v)
