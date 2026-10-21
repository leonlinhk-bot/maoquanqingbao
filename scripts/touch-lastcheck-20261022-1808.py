import json
from datetime import datetime, timezone, timedelta

HKT = timezone(timedelta(hours=8))
NOW = datetime.now(HKT).isoformat(timespec='seconds')
P = '/Users/leonliang/maoquanqingbao/data/last-check.json'
d = json.load(open(P, encoding='utf-8'))
d['lastCheck'] = NOW
for k, v in d['sources'].items():
    v['last'] = NOW
json.dump(d, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('lastCheck ->', NOW, 'sources', len(d['sources']))
