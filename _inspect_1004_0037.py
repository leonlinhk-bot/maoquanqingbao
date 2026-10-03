import json
d = json.load(open('data/live-items.json'))
print('keys:', list(d.keys()))
print('meta:', json.dumps(d.get('meta', {}), ensure_ascii=False)[:1000])
its = d['items']
print('total items:', len(its))
for it in its[:8]:
    print('---')
    t = it.get('title', {})
    print(it.get('id'), '|', it.get('sourceKey'), '|', it.get('publishedAt'), '|', it.get('sourceTier'), '|', it.get('verifyStatus'))
    print('  ', t.get('sc') if isinstance(t, dict) else t)
