import json, os
d=json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
items=d['items']
want=['ia','ia_circular','hkma','hkma_press','govhk','fstb','mpfa','hkfi','aia','manulife','prudential','axa','sunlife','insuranceasia','insuranceasianews','insurancebusinessmag','scmp','artemis','nfra','insurtech','family_office']
for k in want:
    rows=[i for i in items if i.get('sourceKey')==k]
    rows.sort(key=lambda x:(x.get('publishedAt') or ''), reverse=True)
    print(f"\n===== {k}  (n={len(rows)})  newest 4:")
    for i in rows[:4]:
        print('  ', i.get('publishedAt'), '|', (i.get('title') or {}).get('sc','')[:52], '|', (i.get('originalUrl') or '')[:95])
