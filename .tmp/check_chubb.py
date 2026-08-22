import json

d = json.load(open('data/live-items.json'))
for it in d['items']:
    t = it['title']['sc']
    if any(k in t for k in ['Chubb', '安達', '安达', 'chubb']):
        print(it['id'], '|', it.get('sourceKey'), '|', it.get('publishedAt'), '|', t[:70])
print('---')
for it in d['items']:
    if it.get('sourceKey') == 'chubb':
        print(it['id'], '|', it.get('publishedAt'), '|', it['title']['sc'][:60])
