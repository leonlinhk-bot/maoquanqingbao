import json
d = json.load(open('data/live-items.json'))
ids = set()
for it in d['items']:
    ids.add(it['id'])
print('recent items (publishedAt >= 2026-09-30):')
for it in d['items']:
    p = it['publishedAt']
    if p >= '2026-09-30':
        print(f"  {p} | {it['sourceKey']} | {it['id']}")
        print(f"      {it['title']['sc'][:80]}")
print('total', len(d['items']))
