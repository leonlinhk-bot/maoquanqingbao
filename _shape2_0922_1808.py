import json
d=json.load(open('data/live-items.json'))
it=d['items'][0]
print(json.dumps(it,ensure_ascii=False,indent=1)[:2500])
print('--- keys union ---')
ks=set()
for x in d['items'][:50]: ks|=set(x.keys())
print(sorted(ks))
print('--- verifyStatus counts ---')
import collections
print(collections.Counter(x.get('verifyStatus') for x in d['items']))
print('--- contentKind ---')
print(collections.Counter(x.get('contentKind') for x in d['items']))
print('--- boards ---')
c=collections.Counter()
for x in d['items'][:100]:
    for b in x.get('boards',[]): c[b]+=1
print(c)
