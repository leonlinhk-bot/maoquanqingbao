import json, re, html
from datetime import datetime, timezone, timedelta
HKT = timezone(timedelta(hours=8))
D = 'data/_1021_1808/'

print('=== HKMA api sample ===')
hj = json.load(open(D + 'hkma_api.json', encoding='utf-8'))
recs = hj['result']['records']
print('total', len(recs), 'header', list(recs[0].keys()))
for r in recs[:6]:
    print(r.get('date'), '|', r.get('title')[:90], '|', r.get('link'))

def strip(p):
    s = open(p, encoding='utf-8', errors='replace').read()
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S)
    s = re.sub(r'<style.*?</style>', ' ', s, flags=re.S)
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', html.unescape(s))

for name in ['aia', 'pru', 'axa', 'sun', 'nfra']:
    t = strip(D + name + '.html')
    print(f"\n=== {name} ({len(t)} chars) ===")
    # find date-ish tokens with context
    hits = [m for m in re.finditer(r'(2026[-/年]\s?0?9[-/月]\s?\d{1,2}|2026[-/年]\s?10[-/月]\s?\d{1,2}|\d{1,2}\s?(?:Oct|October|10月)\s?2026)', t)]
    print('date-token hits:', len(hits))
    seen = set()
    for m in hits[:14]:
        ctx = t[max(0, m.start()-90):m.end()+60]
        k = ctx[:40]
        if k in seen: continue
        seen.add(k)
        print('  ...', ctx)
