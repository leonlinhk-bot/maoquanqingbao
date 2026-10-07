import json
live=json.load(open('data/live-items.json'))
items=live['items']
for it in items[:2]+items[10:11]:
    print(json.dumps(it, ensure_ascii=False, indent=1))
    print('-'*80)
from collections import Counter
c=Counter()
for it in items[:300]:
    c.update(it.get('themes') or [])
print('themes:', c.most_common(40))
c2=Counter()
for it in items[:300]:
    c2.update(it.get('boards') or [])
print('boards:', c2.most_common())
c3=Counter(it.get('sourceTier') for it in items[:300])
print('tiers:', c3)
c4=Counter(it.get('contentKind') for it in items[:300])
print('kinds:', c4)
