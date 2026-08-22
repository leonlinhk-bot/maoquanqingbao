import json

d = json.load(open('data/live-items.json'))
items = d['items']
# print 3 recent items in full
for it in items[:3]:
    print(json.dumps(it, ensure_ascii=False, indent=1))
    print('-' * 100)
# also check meta format
print('META:', json.dumps(d.get('meta', {}), ensure_ascii=False)[:600])
