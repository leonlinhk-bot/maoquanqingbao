import json
d = json.load(open('data/live-items.json'))
print('keys:', list(d.keys()))
print('meta:', json.dumps(d.get('meta', {}), ensure_ascii=False, indent=1))
items = d['items']
print('items:', len(items))
for it in items[:8]:
    print(it.get('publishedAt'), '|', it.get('sourceKey'), '|', it.get('id'), '|', it.get('sourceTier'), '|', str(it.get('title', {}).get('sc'))[:60])
print('--- last 8 ---')
for it in items[-3:]:
    print(it.get('publishedAt'), '|', it.get('sourceKey'), '|', it.get('id'))
