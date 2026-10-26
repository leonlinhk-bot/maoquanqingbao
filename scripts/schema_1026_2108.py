import json
d = json.load(open('data/live-items.json'))
items = d['items'] if isinstance(d, dict) else d
print(json.dumps(items[0], ensure_ascii=False, indent=1)[:3000])
print('\n--- second (ian pending) ---')
print(json.dumps(items[1], ensure_ascii=False, indent=1)[:2500])
print('\n--- meta full ---')
m = d['meta']
print(json.dumps({k: v for k, v in m.items() if k not in ('sourcesPrimary', 'archive')}, ensure_ascii=False, indent=1)[:1500])
