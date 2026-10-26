import json, collections
d = json.load(open('data/live-items.json'))
items = d['items'] if isinstance(d, dict) else d
t = collections.defaultdict(collections.Counter)
for it in items:
    t[it.get('sourceKey')][it.get('sourceTier')] += 1
for k in ['scmp', 'ian', 'artemis', 'hkma', 'govhk', 'insuranceasia', 'insuranceasianews', 'reinsurancenews', 'ia']:
    print(k, dict(t.get(k, {})))
# boards enum usage
b = collections.Counter()
for it in items:
    for x in it.get('boards') or []:
        b[x] += 1
print('boards', b.most_common())
# sample ian item full
for it in items:
    if it.get('sourceKey') == 'ian':
        print(json.dumps({kk: it[kk] for kk in ('id', 'sourceTier', 'score', 'boards', 'contentKind')}, ensure_ascii=False))
        break
