import json
from collections import Counter
d = json.load(open('/Users/leonliang/maoquanqingbao/data/_raw_1025_0052/all.json'))
print(Counter(i['src'] for i in d).most_common())
nodate = [i for i in d if not i['dt']]
print('no-date:', len(nodate))
for i in nodate[:15]:
    print('  ', i['src'], '|', i['title'][:70])
print('--- gnews newest 20 ---')
g = sorted([i for i in d if i['src'].startswith('gnews') and i['dt']], key=lambda x: x['dt'], reverse=True)
for i in g[:20]:
    print(i['dt'][:16], '|', i['src'], '|', i['title'][:80])
