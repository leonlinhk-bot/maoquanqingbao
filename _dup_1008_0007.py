import json
live=json.load(open('data/live-items.json'))
items=live['items']
# IA-related recent
print('=== items with sourceKey containing ia / govhk / hkfi ===')
for it in items[:60]:
    sk=(it.get('sourceKey') or '')
    if 'ia' in sk.lower() or 'gov' in sk.lower() or 'hkfi' in sk.lower():
        print(it.get('publishedAt'), '|', sk, '|', (it.get('title',{}).get('sc') or '')[:70], '|', it.get('id'))
print()
print('=== all sourceKeys (top 40 by count) ===')
from collections import Counter
c=Counter(it.get('sourceKey') for it in items)
for k,v in c.most_common(45):
    print(v, k)
print()
print('=== IDs matching known candidates ===')
import re
cands=['awbury','mitsui','lockton','knightcorp','ace-insurance','philippines','nhis','sme-cover','hdi','picc','ucits','pacific-life','polo','securis','catiq','montreal','chubb','qbe']
for cand in cands:
    hits=[it['id'] for it in items if cand in (it.get('id','')+json.dumps(it.get('title',{}),ensure_ascii=False)).lower()]
    print(cand, '->', hits[:4])
