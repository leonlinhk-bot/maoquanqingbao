import json
d = json.load(open('data/live-items.json'))
print(json.dumps(d['meta'], ensure_ascii=False, indent=1)[:4000])
