import json
d = json.load(open('data/live-items.json'))
items = d['items']
print('total:', len(items))
for it in items:
    ia = it.get('ingestedAt', '')
    if ia.startswith('2026-08-22'):
        print(ia, '|', it.get('sourceKey'), '|', it.get('sourceTier'), '|', it['id'], '|', it['title']['sc'][:50])
