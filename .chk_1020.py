import json, os, glob
p = 'data/_staging/search-candidates.json'
print('exists:', os.path.exists(p))
if os.path.exists(p):
    d = json.load(open(p))
    items = d if isinstance(d, list) else d.get('candidates', [])
    print('count', len(items))
    for c in items[:20]:
        print(c.get('date'), '|', c.get('tier') or c.get('sourceTier'), '|', c.get('host') or c.get('domain'), '|', (c.get('title') or '')[:80], '|', (c.get('url') or '')[:80])
print('--- staged files ---')
for f in glob.glob('data/_staging/*'):
    print(f, os.path.getmtime(f))

# check for existing disciplinary panel item
live = json.load(open('data/live-items.json'))
for it in live['items']:
    t = it.get('title', {}).get('sc', '')
    if '紀律' in t or '纪律' in t or 'Disciplinary' in t:
        print('DUP?', it['id'], it['publishedAt'], t[:80])
