import json, re
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
items = d['items']
terms = ['Mox', 'BOCG', '中銀集團保險', 'BOC Group', 'underwriting profit', '253', 'captive', '自保', 'Vietnam', '越南',
         'Abu Dhabi', '阿布扎比', 'foreign broker', '外資經紀', 'week in insurance', '稅務', 'tax crackdown', '275.2', '2752']
for t in terms:
    hits = [i for i in items if t.lower() in json.dumps(i, ensure_ascii=False).lower()]
    print(f'--- {t}: {len(hits)}')
    for h in hits[:4]:
        print('    ', h['id'], '|', h.get('publishedAt'), '|', h['title']['sc'][:60])
print('\n--- ids published >= 2026-10-22 with title ---')
for i in items:
    if (i.get('publishedAt') or '') >= '2026-10-22':
        print(i['publishedAt'][:16], '|', i['id'], '|', i['title']['sc'][:60])
