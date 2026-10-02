import json
d = json.load(open('data/live-items.json'))
items = d['items']
cut = '2026-10-01T18:00:00'
print('--- items with publishedAt >= %s ---' % cut)
n = 0
for it in items:
    pa = it.get('publishedAt', '')
    if pa >= cut:
        n += 1
        print(pa, '|', it.get('sourceKey'), '|', it['id'])
print('total recent:', n)
print()
print('--- date-only / malformed publishedAt in top 60 ---')
for it in items[:60]:
    pa = it.get('publishedAt', '')
    if len(pa) < 16:
        print(pa, '|', it['id'])
