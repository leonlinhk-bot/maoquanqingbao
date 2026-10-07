import json
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json', encoding='utf-8'))
seen = set()
for it in d['items']:
    k = it.get('sourceKey')
    if k in ('hkma','insuranceasianews','govhk','nfra','ia','mpfa') and k not in seen:
        seen.add(k)
        print(k, '|', it['id'], '|', it.get('sourceTier'), it.get('score'), '|', it.get('contentKind'), '| lang', it.get('source',{}).get('lang'))
        print('   ', it['source']['sc'][:60], '|', it['title']['sc'][:60])
        print('   boards', it.get('boards'), 'themes', it.get('themes'))
print()
print('most recent hkma items:')
n = 0
for it in d['items']:
    if it.get('sourceKey') == 'hkma':
        print('  ', it['id'], it.get('publishedAt'), it['title']['sc'][:70], '|', it.get('sourceTier'), it.get('score'))
        n += 1
        if n >= 4: break
print('most recent ian items:')
n = 0
for it in d['items']:
    if it.get('sourceKey') == 'insuranceasianews':
        print('  ', it['id'], it.get('publishedAt'), it['title']['sc'][:70], '|', it.get('sourceTier'), it.get('score'))
        n += 1
        if n >= 4: break
