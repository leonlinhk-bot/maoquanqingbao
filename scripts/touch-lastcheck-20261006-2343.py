#!/usr/bin/env python3
import json
from datetime import datetime, timezone, timedelta
NOW = datetime.now(timezone(timedelta(hours=8))).strftime('%Y-%m-%dT%H:%M:%S+08:00')
p='/Users/leonliang/maoquanqingbao/data/last-check.json'
d=json.load(open(p,encoding='utf-8'))
d['lastCheck']=NOW
for k,v in d['sources'].items():
    v['last']=NOW
json.dump(d, open(p,'w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('last-check updated ->', NOW, '| sources:', len(d['sources']))
