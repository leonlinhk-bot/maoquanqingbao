import json
from collections import Counter
live=json.load(open('data/live-items.json'))
items=live['items']
c=Counter((it.get('publishedAt') or '')[:10] for it in items)
for d in sorted(c)[-21:]:
    print(d, c[d])
print()
# id dedup check for candidates
cands=['awbury','alice-lim','kenichiro','zurich','beazley','kunzmann','orang','markel','kcc-','isaias','twia','rvs','calpers','althoff','moodys','pacific-life-re','21-8bn','sme','nhis']
for cand in cands:
    hits=[it['id'] for it in items if cand in it.get('id','').lower()]
    print(cand, '->', hits[:5])
