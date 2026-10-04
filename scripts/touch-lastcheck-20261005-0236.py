# -*- coding: utf-8 -*-
import json, datetime
NOW = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).replace(microsecond=0).isoformat()
p = 'data/last-check.json'
d = json.load(open(p))
d['lastCheck'] = NOW
for k, v in d.get('sources', {}).items():
    v['last'] = NOW
json.dump(d, open(p, 'w'), ensure_ascii=False, indent=2)
print('lastCheck ->', NOW, '| sources:', len(d.get('sources', {})))
