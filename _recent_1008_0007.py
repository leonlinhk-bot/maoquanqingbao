import json
live=json.load(open('data/live-items.json'))
items=live['items']
for key in ['artemis','insuranceasia','ibm','insurancebusinessmag','insuranceasianews']:
    print('='*15, key)
    rows=[it for it in items if (it.get('sourceKey') or '')==key]
    rows.sort(key=lambda x: x.get('publishedAt',''), reverse=True)
    for it in rows[:10]:
        print(it.get('publishedAt'), '|', it.get('id'), '|', (it.get('title',{}).get('sc') or '')[:65])
