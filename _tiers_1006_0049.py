import json
from collections import Counter, defaultdict
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
items = d['items']
tier = defaultdict(Counter)
sk = defaultdict(Counter)
for it in items:
    tier[it.get('sourceKey')][it.get('sourceTier')] += 1
    for t in (it.get('themes') or []):
        sk['THEMES'][t] += 1
    for b in (it.get('boards') or []):
        sk['BOARDS'][b] += 1
for k in ('insuranceasia', 'insuranceasianews', 'artemis', 'insurancebusinessmag', 'scmp', 'ia', 'hkma', 'family_office', 'nfra', 'insurtech', 'aia', 'sunlife', 'prudential', 'manulife', 'axa', 'businessstandard', 'epochtimes'):
    print(k, dict(tier.get(k, {})))
print('\nBOARDS:', dict(sk['BOARDS']))
print('\nTOP THEMES:', [t for t, c in sk['THEMES'].most_common(70)])
