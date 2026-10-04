import json
d = json.load(open('data/live-items.json'))
ids = [it['id'] for it in d['items']]
for k in ['fwd', 'income-insurance', 'citi', 'family-office-forum', 'forum', 'week', 'iaasia-', 'hkfi']:
    hits = [i for i in ids if k in i.lower()]
    print(f'[{k}] {len(hits)}: {hits[:14]}')
# show items published on/after 2026-10-02 with sourceKey stats
from collections import Counter
c = Counter(it.get('sourceKey') for it in d['items'] if (it.get('publishedAt') or '') >= '2026-10-01')
print('sourceKey since Oct 1:', dict(c))
