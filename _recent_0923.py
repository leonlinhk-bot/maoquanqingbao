import json
d = json.load(open('data/live-items.json'))
items = d['items']
recent = [i for i in items if (i.get('publishedAt') or '') >= '2026-09-15']
print('recent count', len(recent))
for i in sorted(recent, key=lambda x: x.get('publishedAt') or ''):
    print((i.get('publishedAt') or '')[:16], '|', i.get('sourceKey'), '|', i['id'])
print()
print('TOTAL', len(items))
