import json, datetime
P='/Users/leonliang/maoquanqingbao/data/last-check.json'
HKT=datetime.timezone(datetime.timedelta(hours=8))
now=datetime.datetime.now(HKT).replace(second=0,microsecond=0).isoformat()
d=json.load(open(P))
d['lastCheck']=now
for k,v in d.get('sources',{}).items():
    v['last']=now
json.dump(d,open(P,'w'),ensure_ascii=False,indent=2)
print('lastCheck ->',now,'sources',len(d['sources']))
