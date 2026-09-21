import json,sys
d=json.load(open('data/live-items.json'))
items=d['items']
kws=["Beazley","Zurich","Typhoon","Dujuan","Nippon","Airline","Marine war","FWD","Protec","Aurenity","Kota","InsuranceDekho","P&C reinsurance","Singapore","Japan","Japan's"]
for k in kws:
    hits=[(it.get('publishedAt'),it.get('title',{}).get('sc','')[:70],it.get('originalUrl','')) for it in items[:120] if k.lower() in (it.get('title',{}).get('sc','')+it.get('title',{}).get('tc','')).lower()]
    print('==',k,len(hits))
    for h in hits[:4]:
        print('   ',h[0],'|',h[1])
# also list all ids
ids=[it.get('id') for it in items]
print('last 40 ids count', len(ids))
for i in ids[:40]: print(i)
