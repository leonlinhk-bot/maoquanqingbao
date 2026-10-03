import json, re
live = json.load(open('data/live-items.json'))
its = live['items']
for kw in ['premium financing', '保費融資', '保费融资', '融资']:
    hits = [i for i in its if kw.lower() in json.dumps(i, ensure_ascii=False).lower()]
    print(f'--- {kw}: {len(hits)} ---')
    for i in hits[:5]:
        t = i.get('title', {})
        print('  ', i.get('publishedAt'), '|', i.get('sourceKey'), '|', (t.get('sc') if isinstance(t, dict) else t)[:100])
