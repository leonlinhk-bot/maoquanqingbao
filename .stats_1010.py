import json, collections
d = json.load(open('data/live-items.json'))
it = d['items']
rec = [x for x in it if str(x.get('publishedAt', ''))[:10] >= '2026-10-08']
print('recent', len(rec))
ls = sorted(len((x.get('summary') or {}).get('sc', '')) for x in rec)
print('summary len min/med/max:', ls[0], ls[len(ls) // 2], ls[-1])
keys = collections.Counter()
for x in rec:
    for k in x: keys[k] += 1
print(keys)
print('verifyStatus:', collections.Counter(x.get('verifyStatus') for x in rec))
print('sourceTier:', collections.Counter(x.get('sourceTier') for x in rec))
print('boards:', collections.Counter(b for x in rec for b in x.get('boards', [])))
print('contentKind:', collections.Counter(x.get('contentKind') for x in rec))
print('score range:', min(x.get('score', 0) for x in rec), max(x.get('score', 0) for x in rec))
print('lang:', collections.Counter((x.get('source') or {}).get('lang') for x in rec))
print('featured count:', sum(1 for x in rec if x.get('featured')))
print('--- sample ids/themes ---')
for x in rec[:6]:
    print(x['id'], x.get('themes'), x.get('boards'), x.get('sourceKey'), x.get('contentKind'))
