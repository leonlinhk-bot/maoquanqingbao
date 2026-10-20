import json
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
for k in ['insuranceasia', 'insuranceasianews', 'reinsurancenews', 'artemis']:
    print('##', k)
    c = 0
    for it in d['items']:
        if it.get('sourceKey') == k:
            print('  ', it['publishedAt'][:16], it.get('sourceTier'), it.get('score'), it.get('contentKind'), it['title']['sc'][:50])
            c += 1
            if c >= 6:
                break
