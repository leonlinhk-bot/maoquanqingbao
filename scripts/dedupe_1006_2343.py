import json
d=json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
items=d['items']
keys=['虛擬投資','積金局','10.3','DPP','紀律處分委員會','最自由經濟體','馬來西亞中央銀行','Bank Negara','中銀香港','線上人壽','Prismic','Beazley','Allianz','Canopius','Castle','Markel','Paul Gardner','Swiss Re CorSo','Adnan','El Nino','印度','Canopius','CatIQ','Arbol','VisionFund','Hannover','CalPERS','陳德翹','樂山','德林','eMPF','積金易','Tower','Meritz','科技保险','信息披露','HSBC','滙豐','AI中心','柏太陽','財富','Moody','Tower']
for k in keys:
    hits=[]
    for i in items:
        s=(i['id']+' '+(i.get('title') or {}).get('sc','')+' '+(i.get('title') or {}).get('tc','')+' '+(i.get('originalUrl') or ''))
        if k.lower() in s.lower():
            hits.append((i.get('publishedAt'), i['id']))
    if hits:
        print(f'== {k}: {len(hits)} hits; newest 3:')
        for h in sorted(hits, reverse=True)[:3]: print('    ', h[0], h[1])
