import json, re
d = json.load(open('data/live-items.json'))
items = d['items']
# search for IA enforcement / recent IA items
pats = ['Jian Yongqin', 'Jian', 'enforcement', '紀律', '处分', '處分', 'suspends']
for it in items:
    t = (it.get('title', {}).get('sc') or '') + ' ' + (it.get('title', {}).get('tc') or '')
    if any(p in t for p in pats):
        print(it.get('publishedAt'), '|', it.get('sourceKey'), '|', t[:90])
print('---- IA items since 2026-10-01 ----')
for it in items:
    if it.get('sourceKey') == 'ia' and (it.get('publishedAt') or '') >= '2026-10-01':
        print(it.get('publishedAt'), '|', it.get('title', {}).get('sc')[:90])
print('---- urls containing enforcement ----')
for it in items:
    if 'enforcement' in (it.get('originalUrl') or ''):
        print(it.get('publishedAt'), '|', it.get('originalUrl'))
