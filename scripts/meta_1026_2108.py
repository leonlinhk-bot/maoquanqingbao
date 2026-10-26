import json
d = json.load(open('data/live-items.json'))
m = d['meta']
for k, v in m.items():
    s = json.dumps(v, ensure_ascii=False)
    print(k, '=', s[:300])
