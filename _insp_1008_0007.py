import json, os, glob
p='data/live-items.json'
d=json.load(open(p))
print('keys:', list(d.keys()))
print('meta:', json.dumps(d.get('meta'), ensure_ascii=False))
items=d.get('items',[])
print('items:', len(items))
for it in items[:12]:
    print(it.get('id'), '|', it.get('publishedAt'), '|', it.get('sourceKey'), '|', it.get('verifyStatus'), '|', it.get('sourceTier'))
print('--- oldest 3 ---')
for it in items[-3:]:
    print(it.get('id'), '|', it.get('publishedAt'), '|', it.get('sourceKey'))
print('--- posters latest ---')
ps=sorted(glob.glob('posters/*'))
print(ps[-6:])
print('--- scripts publish/rebuild ---')
print([f for f in os.listdir('scripts') if 'publish' in f or 'rebuild' in f or 'poster' in f])
