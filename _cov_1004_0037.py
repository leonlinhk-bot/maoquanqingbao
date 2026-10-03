import json
live = json.load(open('data/live-items.json'))
its = live['items']
from collections import Counter
c = Counter(i.get('sourceKey') for i in its)
print('sourceKey counts (top 25):')
for k, v in c.most_common(25):
    print(f'  {k}: {v}')
print()
for sk in ['ia', 'hkma', 'aia', 'manulife', 'prudential', 'axa', 'sunlife', 'insurance_asia', 'insuranceasia', 'nfra', 'scmp', 'artemis', 'hkfi', 'insuranceasianews', 'insurancebusinessmag', 'insurtech', 'family_office']:
    sub = [i for i in its if i.get('sourceKey') == sk]
    if not sub:
        print(f'{sk}: NONE')
        continue
    sub.sort(key=lambda x: str(x.get('publishedAt', '')), reverse=True)
    t = sub[0].get('title', {})
    print(f'{sk}: n={len(sub)} latest={sub[0].get("publishedAt")} :: {(t.get("sc") if isinstance(t, dict) else t)[:80]}')
