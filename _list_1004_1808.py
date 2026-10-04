import json
d = json.load(open('data/live-items.json'))
rows = sorted([it for it in d['items'] if (it.get('publishedAt') or '') >= '2026-10-02'], key=lambda x: x['publishedAt'], reverse=True)
print('count since 10-02:', len(rows))
for it in rows:
    print(it['publishedAt'], '|', it.get('sourceKey'), '|', it['id'])
