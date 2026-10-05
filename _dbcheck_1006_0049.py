import json
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
items = d['items']
print('=== items with sourceKey in (ia, aia, sunlife, prudential, axa, manulife, hkma, artemis, insuranceasianews, insuranceasia) with publishedAt >= 2026-09-20 ===')
keys = ('ia', 'aia', 'sunlife', 'prudential', 'axa', 'manulife', 'hkma', 'insuranceasianews', 'insuranceasia')
for it in items:
    if it.get('sourceKey') in keys and (it.get('publishedAt') or '') >= '2026-09-20':
        print(it.get('publishedAt'), '|', it.get('sourceKey'), '|', it.get('id'))
        print('     ', (it.get('title') or {}).get('sc', '')[:90])
        print('      URL:', it.get('originalUrl'))
