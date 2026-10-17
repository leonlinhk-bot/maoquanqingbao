import json
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json', encoding='utf-8'))
for key in ['nfra', 'ia', 'hkfi', 'scmp', 'family_office', 'insurtech']:
    its = [it for it in d['items'] if it['sourceKey'] == key]
    print('==', key, len(its))
    for it in its[:4]:
        print('   ', it['publishedAt'][:16], it['title']['sc'][:70], '|', it['originalUrl'][:90])
