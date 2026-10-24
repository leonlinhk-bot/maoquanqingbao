import json, os
base = '/Users/leonliang/maoquanqingbao/data/_raw_1025_0044/'
d = json.load(open(base + 'ds_search.json'))
print(type(d), (list(d.keys()) if isinstance(d, dict) else len(d)))
print(json.dumps(d, ensure_ascii=False)[:1200])
