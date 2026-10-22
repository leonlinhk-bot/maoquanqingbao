import json
from datetime import datetime, timezone, timedelta

HKT = timezone(timedelta(hours=8))
now = datetime.now(HKT).replace(microsecond=0).isoformat()

P = '/Users/leonliang/maoquanqingbao/data/last-check.json'
d = json.load(open(P, encoding='utf-8'))
d['lastCheck'] = now
for k, v in d['sources'].items():
    v['last'] = now
json.dump(d, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('lastCheck ->', now, 'sources:', len(d['sources']))
