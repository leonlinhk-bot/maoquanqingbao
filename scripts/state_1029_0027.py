import json
from collections import Counter
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
items = d['items']
print('total items:', len(items))
print('meta keys:', list(d.get('meta', {}).keys()))
print('meta:', json.dumps(d.get('meta', {}), ensure_ascii=False))
print('max publishedAt:', max(i['publishedAt'] for i in items))
c = Counter(i['publishedAt'][:10] for i in items)
for k in sorted(c)[-8:]:
    print(' ', k, c[k])
print('--- last 12 items (title + publishedAt + sourceKey) ---')
for i in items[:12]:
    print(i['publishedAt'], '|', i.get('sourceKey'), '|', i['title']['sc'][:60])
