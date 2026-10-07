import json
from collections import Counter
d=json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
its=d['items']
for k in ['contentRole','evergreen','featured','contentKind','sourceTier']:
    print(k, dict(Counter(str(i.get(k)) for i in its)))
print('\nsample ingestedAt:', json.dumps(its[0].get('ingestedAt'), ensure_ascii=False))
print('sample evergreen:', its[0].get('evergreen'), 'featured:', its[0].get('featured'), 'contentRole:', its[0].get('contentRole'))
