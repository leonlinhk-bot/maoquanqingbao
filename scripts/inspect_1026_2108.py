import json, collections
d = json.load(open('data/live-items.json'))
items = d['items'] if isinstance(d, dict) else d
print('total', len(items))
print('meta.generatedAt', d['meta'].get('generatedAt'))
print('meta.itemCount', d['meta'].get('itemCount'))
print('--- first 12 ---')
for it in items[:12]:
    print(it.get('publishedAt'), '|', it.get('sourceKey'), '|', it.get('title',{}).get('sc','')[:50])
print('--- ids with publishedAt >= 2026-10-24 ---')
cnt = collections.Counter()
for it in items:
    p = it.get('publishedAt') or ''
    if p >= '2026-10-24':
        print(p, '|', it.get('sourceKey'), '|', it.get('verifyStatus'), '|', it.get('title',{}).get('sc','')[:46])
        cnt[it.get('sourceKey')] += 1
print('counts', dict(cnt))
print('--- all sourceKey tally (top 30) ---')
c2 = collections.Counter(it.get('sourceKey') for it in items)
print(c2.most_common(30))
