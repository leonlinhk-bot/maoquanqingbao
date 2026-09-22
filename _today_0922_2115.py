import json
d = json.load(open('data/live-items.json'))
items = d['items']
todays = [it for it in items if str(it.get('publishedAt', '')).startswith('2026-09-22')]
print('today (2026-09-22) items:', len(todays))
for it in todays:
    print(it.get('publishedAt'), '|', it.get('sourceKey'), '|', it.get('id'), '|', it.get('title', {}).get('sc', '')[:50], '|', it.get('originalUrl', '')[:90])
