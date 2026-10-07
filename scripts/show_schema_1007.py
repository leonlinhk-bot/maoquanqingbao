import json
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json', encoding='utf-8'))
print(json.dumps(d['items'][0], ensure_ascii=False, indent=1))
print('----- second -----')
print(json.dumps(d['items'][3], ensure_ascii=False, indent=1))
print('----- meta keys -----')
print(list(d.keys()), list(d['meta'].keys()))
print(json.dumps({k: v for k, v in d['meta'].items() if k not in ('sourcesPrimary',)}, ensure_ascii=False)[:1200])
