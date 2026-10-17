import json
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json', encoding='utf-8'))
for it in d['items']:
    s = it['title']['sc'] + it.get('summary', {}).get('sc', '')
    if 'IAIS' in s:
        print(it['publishedAt'], it['sourceKey'], it['title']['sc'])
        print('  ', it['summary']['sc'][:300])
        print('  ', it['originalUrl'])
