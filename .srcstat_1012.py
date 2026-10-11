import json
from collections import defaultdict
d=json.load(open('data/live-items.json'))
items=d['items']
by=defaultdict(list)
for it in items:
    by[it.get('sourceKey')].append(it.get('publishedAt') or '')
print('distinct sourceKeys:', len(by))
for k,v in sorted(by.items(), key=lambda kv: max(kv[1]), reverse=True):
    print('%-22s n=%-4d latest=%s' % (k, len(v), max(v)))
