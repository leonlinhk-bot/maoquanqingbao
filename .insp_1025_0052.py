import json
from collections import Counter

d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
print('meta:', json.dumps(d.get('meta', {}), ensure_ascii=False)[:800])
print('items:', len(d['items']))
print('top-level keys:', list(d.keys()))
print('--- newest 12 ---')
for it in d['items'][:12]:
    print(it['id'], '|', it.get('sourceKey'), '|', it.get('publishedAt'), '|', it.get('sourceTier'), '|', it['title']['sc'][:50])
print('--- sourceKey counts ---')
print(Counter(i.get('sourceKey') for i in d['items']).most_common(40))
print('--- sample full item ---')
print(json.dumps(d['items'][0], ensure_ascii=False, indent=1)[:2500])
