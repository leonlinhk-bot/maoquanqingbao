import json
d=json.load(open('data/live-items.json'))
for it in d['items'][:4]:
    print('='*70)
    print('id:', it['id'], '|', it['publishedAt'], '|', it['sourceTier'], '|', it['score'], it['verifyStatus'])
    print('title.sc:', it['title']['sc'])
    print('title.tc:', it['title']['tc'])
    print('len summary sc/tc:', len(it['summary']['sc']), len(it['summary']['tc']))
    print('why.tc:', it['why']['tc'][:120])
    print('actions.front:', it['actions']['front'])
    print('tags:', it['tags'])
    print('boards:', it['boards'], 'themes:', it['themes'], 'roles:', it['rolesImpact'])
    print('source:', json.dumps(it['source'], ensure_ascii=False))
    print('url:', it['originalUrl'])
