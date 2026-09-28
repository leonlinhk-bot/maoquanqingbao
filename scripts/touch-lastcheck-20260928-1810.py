import json, datetime
p = 'data/last-check.json'
d = json.load(open(p, encoding='utf-8'))
now = '2026-09-28T18:10:00+08:00'
d['lastCheck'] = now
for k, v in d['sources'].items():
    v['last'] = now
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('last-check updated:', now, 'sources=', len(d['sources']))
