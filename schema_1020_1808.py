import json
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
it = d['items'][0]
print(json.dumps(it, ensure_ascii=False, indent=1))
print('\n--- keys of all items union ---')
keys = set()
for x in d['items']:
    keys |= set(x.keys())
print(sorted(keys))
print('\n--- meta ---')
print(json.dumps(d['meta'], ensure_ascii=False, indent=1)[:2000])
print('\n--- top-level keys ---', list(d.keys()))
