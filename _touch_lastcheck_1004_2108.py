# -*- coding: utf-8 -*-
import json, datetime
live = json.load(open('data/live-items.json', encoding='utf-8'))['items']
blob = json.dumps(live, ensure_ascii=False).lower()
for t in ['conduct in focus', '社交媒体', '社交媒體', 'sandbox++', '反洗钱', 'aml']:
    print(t, '->', 'FOUND' if t in blob else 'NOT')

TZ = datetime.timezone(datetime.timedelta(hours=8))
NOW = datetime.datetime.now(TZ).strftime('%Y-%m-%dT%H:%M:%S+08:00')
lp = 'data/last-check.json'
lc = json.load(open(lp, encoding='utf-8'))
lc['lastCheck'] = NOW
for k, v in lc.get('sources', {}).items():
    v['last'] = NOW
json.dump(lc, open(lp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('last-check.json updated ->', NOW, '| sources:', len(lc.get('sources', {})))
