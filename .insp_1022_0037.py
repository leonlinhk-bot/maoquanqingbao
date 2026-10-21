import json, collections
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
items = d['items'] if isinstance(d, dict) else d
print('total:', len(items))
print('meta:', json.dumps(d.get('meta', {}), ensure_ascii=False)[:400] if isinstance(d, dict) else 'n/a')
print('keys of item0:', list(items[0].keys()))
for it in items[:6]:
    print(it['id'], '|', it.get('publishedAt'), '|', it['title']['sc'][:45])
print('--- by date ---')
c = collections.Counter((it.get('publishedAt') or '')[:10] for it in items)
for k in sorted(c)[-8:]:
    print(k, c[k])
print('--- sourceKey last 30 ---')
for it in items[:30]:
    print(it.get('sourceKey'), '|', (it.get('publishedAt') or '')[:10], '|', it['title']['sc'][:30])
