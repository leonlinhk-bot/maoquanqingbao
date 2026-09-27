import json, datetime
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
items = d['items']
print('total', len(items))
print('--- items publishedAt >= 2026-09-24 ---')
for it in items:
    pa = it.get('publishedAt') or ''
    if pa >= '2026-09-24':
        t = it.get('title')
        t = t.get('sc') if isinstance(t, dict) else t
        print(pa, '|', it.get('id'), '|', it.get('sourceKey'), '|', (t or '')[:60])
print()
print('--- 2026-09-27 weekday ---')
print(datetime.date(2026,9,27).strftime('%A'))
print('--- last 12 ingestedAt ---')
ing = sorted({it.get('ingestedAt','') for it in items})
print(ing[-8:])
