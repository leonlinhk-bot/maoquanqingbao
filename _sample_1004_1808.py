import json
d = json.load(open('data/live-items.json'))
for it in d['items'][:6]:
    print(json.dumps(it, ensure_ascii=False, indent=1))
    print('-' * 70)
