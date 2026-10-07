import json
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json', encoding='utf-8'))
print('top keys:', list(d.keys()))
print('meta keys:', list(d['meta'].keys()))
print(json.dumps(d['meta'], ensure_ascii=False)[:1500])
print()
for it in d['items']:
    if it.get('sourceKey') in ('insuranceasia','insurancebusinessmag','hkma','scmp'):
        print(it['id'], '|', it.get('sourceTier'), it.get('score'), '|', it.get('source',{}).get('lang'), '|', it['source']['sc'][:45], '|', it['title']['sc'][:55])
        print('   boards', it.get('boards'), 'themes', it.get('themes'), '| contentRole', it.get('contentRole'), '| featured', it.get('featured'), it.get('evergreen'))
        if it['id'].startswith('insuranceasia'): break
