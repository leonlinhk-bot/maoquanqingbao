import json
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
m = {}
for it in d['items']:
    m.setdefault(it.get('sourceKey'), set()).add(it.get('sourceTier'))
for k in sorted(m):
    print(k, m[k])
print()
# sample scores per source
import collections
sc = collections.defaultdict(list)
for it in d['items']:
    sc[it.get('sourceKey')].append(it.get('score'))
for k in ['insuranceasianews', 'insuranceasia', 'artemis', 'reinsurancenews', 'asiainsurancereview']:
    v = [x for x in sc.get(k, []) if isinstance(x, int)]
    if v:
        print(k, 'n=', len(v), 'min', min(v), 'max', max(v), 'avg', round(sum(v)/len(v)))
