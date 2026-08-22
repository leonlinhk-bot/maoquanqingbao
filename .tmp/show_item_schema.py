import json
d = json.load(open('data/live-items.json'))
items = d['items']
# print 3 most recent full items to see exact schema
for it in items[:3]:
    print(json.dumps(it, ensure_ascii=False, indent=1))
    print('='*80)
