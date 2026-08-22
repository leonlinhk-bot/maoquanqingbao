import json
d = json.load(open('data/live-items.json'))
items = d['items']
print('total items:', len(items))
print('meta:', json.dumps(d.get('meta', {}), ensure_ascii=False)[:400])
print('---top 5---')
for it in items[:5]:
    sk = it.get('sourceKey', it.get('source', ''))
    print(it['id'], '|', it.get('publishedAt', ''), '|', sk, '|', it['title']['sc'][:50])
print('---existing ids---')
ids = set(it['id'] for it in items)
print('count ids:', len(ids))
# existing sourceKeys
from collections import Counter
cks = Counter(it.get('sourceKey', '') for it in items)
print(cks.most_common(30))
