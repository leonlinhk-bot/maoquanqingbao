import json, re
d = json.load(open('data/live-items.json'))
items = d['items']
def find(kw, since='2026-09-25'):
    print(f'--- {kw} ---')
    hit = False
    for it in items:
        blob = json.dumps(it, ensure_ascii=False)
        if kw.lower() in blob.lower() and (it.get('publishedAt') or '') >= since:
            print(' ', it.get('publishedAt'), '|', it.get('sourceKey'), '|', it.get('title', {}).get('sc')[:70])
            hit = True
    if not hit:
        print('  (none)')

for kw in ['Jian', 'Jian Yongqin', 'AML', '洗錢', '洗钱', 'Bolttech', '保特', 'sidecar', '側掛車', '侧挂车', 'PERILS', 'Arbol', 'cat bond', '巨災債券', 'APEC', 'Muse']:
    find(kw)
