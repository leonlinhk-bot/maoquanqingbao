import json
P = '/Users/leonliang/maoquanqingbao/data/last-check.json'
NOW = '2026-10-20T18:08:00+08:00'
d = json.load(open(P, encoding='utf-8'))
d['lastCheck'] = NOW
n = 0
for k, v in d.get('sources', {}).items():
    v['last'] = NOW
    n += 1
json.dump(d, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('updated sources:', n, 'lastCheck:', d['lastCheck'])
