import json, datetime, shutil, os
BASE = '/Users/leonliang/maoquanqingbao'
p = os.path.join(BASE, 'data/last-check.json')
d = json.load(open(p, encoding='utf-8'))
NOW = '2026-09-29T18:10:00+08:00'
d['lastCheck'] = NOW
changed = 0
for k, v in d['sources'].items():
    if isinstance(v, dict):
        v['last'] = NOW
        changed += 1
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('updated sources:', changed, '| lastCheck =', d['lastCheck'])
