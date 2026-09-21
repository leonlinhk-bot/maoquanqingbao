import json
d=json.load(open('data/live-items.json'))
items=d['items']
print(json.dumps(items[0],ensure_ascii=False,indent=1)[:3000])
print('=== FWD items ===')
for it in items[:300]:
    t=(it.get('title',{}).get('sc','')+it.get('title',{}).get('tc',''))
    if 'FWD' in t or '富卫' in t or '富衛' in t:
        print(json.dumps(it,ensure_ascii=False)[:900])
        print('---')
