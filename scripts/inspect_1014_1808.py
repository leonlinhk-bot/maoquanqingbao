#!/usr/bin/env python3
import json, collections
d = json.load(open('data/live-items.json'))
items = d['items']
print('total items:', len(items))
print('meta:', json.dumps(d.get('meta', {}), ensure_ascii=False)[:800])
print('--- first 25 ---')
for it in items[:25]:
    print(it.get('publishedAt'), '|', it.get('sourceKey'), '|', it.get('id'), '|', (it.get('title', {}) or {}).get('sc', '')[:60])
print('--- publishedAt date histogram (top 10) ---')
c = collections.Counter((it.get('publishedAt') or '')[:10] for it in items)
for k, v in sorted(c.items(), reverse=True)[:10]:
    print(k, v)
print('--- sourceKey histogram ---')
c2 = collections.Counter(it.get('sourceKey') for it in items)
for k, v in c2.most_common(30):
    print(k, v)
