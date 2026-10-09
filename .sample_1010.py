import json
d = json.load(open('data/live-items.json'))
it = d['items']
for x in it[:3]:
    print(json.dumps(x, ensure_ascii=False, indent=1))
    print('==========================================')
print('META keys:', json.dumps({k: (v if not isinstance(v, (list, dict)) else type(v).__name__) for k, v in d['meta'].items()}, ensure_ascii=False)[:1200])
