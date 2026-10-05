import json
d = json.load(open('data/live-items.json'))
for it in d['items'][:3]:
    print(json.dumps(it, ensure_ascii=False, indent=1))
    print('-' * 60)
print('META KEYS:', list(d.keys()))
print('FULL META:', json.dumps({k: v for k, v in d['meta'].items() if k != 'sourcesPrimary'}, ensure_ascii=False)[:1500])
