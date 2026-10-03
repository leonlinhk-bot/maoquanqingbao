import json
d = json.load(open('data/live-items.json'))
print(json.dumps(d['items'][1], ensure_ascii=False, indent=1))
print('--- keys ---', list(d.keys()))
print('--- meta keys ---', list(d['meta'].keys()))
for k in ['Ant Health', 'JUST FEEL', '感講', 'eSun寶']:
    hits = [it['id'] for it in d['items'] if k in json.dumps(it, ensure_ascii=False)]
    print(k, '->', hits[:5])
