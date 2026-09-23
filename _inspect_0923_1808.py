import json
d = json.load(open('data/live-items.json'))
items = d['items']
print('total', len(items))
print('meta keys', list(d['meta'].keys()))
print('generatedAt', d['meta'].get('generatedAt'))
# items are newest-first presumably
for i in items[:20]:
    print(i['id'], '|', i.get('publishedAt'), '|', i.get('sourceKey'), '|', i['title']['sc'][:50])
print('--- oldest 3')
for i in items[-3:]:
    print(i['id'], '|', i.get('publishedAt'))
# sourceKey coverage in latest 60
from collections import Counter
print(Counter([x.get('sourceKey') for x in items[:60]]))
