import json
from datetime import datetime, timedelta
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
items = d['items']
print('total', len(items))
print('\n=== items with publishedAt >= 2026-09-28 (by date) ===')
rows = []
for it in items:
    pa = it.get('publishedAt') or ''
    if pa >= '2026-09-28':
        rows.append((pa, it.get('sourceKey'), it.get('id'), (it.get('title') or {}).get('sc','')[:58]))
rows.sort(reverse=True)
for r in rows:
    print(' | '.join(str(x) for x in r))
print('\n=== sourceKey counts (last 30d) ===')
from collections import Counter
c = Counter(it.get('sourceKey') for it in items if (it.get('publishedAt') or '') >= '2026-09-06')
for k, v in c.most_common(40):
    print(f'  {k:26} {v}')
