import json
d = json.load(open('data/live-items.json'))
it = d['items'][0]
print(json.dumps(it, ensure_ascii=False, indent=2))
print('=== meta ===')
m = d['meta']
for k in ('generatedAt','itemCount','windowNote','asOf','changelog'):
    print(k, ':', json.dumps(m.get(k), ensure_ascii=False)[:600])
