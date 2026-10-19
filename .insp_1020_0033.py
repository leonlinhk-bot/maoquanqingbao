import json, collections
d = json.load(open('data/live-items.json'))
print('type:', type(d).__name__)
if isinstance(d, dict):
    print('keys:', list(d.keys()))
    print('meta:', json.dumps(d.get('meta', {}), ensure_ascii=False)[:1500])
    items = d.get('items', [])
else:
    items = d
print('items:', len(items))
for it in items[:8]:
    print('---')
    print(it.get('id'), '|', it.get('publishedAt'), '|', it.get('sourceKey'), '|', it.get('sourceTier'), '|', it.get('publishedAt','')[:10])
    print('  T:', it.get('title', {}).get('sc', '')[:90])
print('date dist:', collections.Counter([i.get('publishedAt','')[:10] for i in items]).most_common(10))
print('sourceKey dist:', collections.Counter([i.get('sourceKey','') for i in items]).most_common(40))
print('last item full:')
print(json.dumps(items[0], ensure_ascii=False, indent=1)[:2500])
