import json
P = 'data/live-items.json'
d = json.load(open(P, encoding='utf-8'))
for it in d['items']:
    if it['id'] == 'rn-france-riots-srcc-20261019':
        it['boards'] = ['market']
        print('fixed boards ->', it['boards'])
json.dump(d, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ok')
