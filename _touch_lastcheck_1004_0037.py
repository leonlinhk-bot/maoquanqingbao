import json, datetime

now = datetime.datetime.now().astimezone().replace(microsecond=0).isoformat()
p = 'data/last-check.json'
d = json.load(open(p))
d['lastCheck'] = now
for k, v in d.get('sources', {}).items():
    v['last'] = now
json.dump(d, open(p, 'w'), ensure_ascii=False, indent=2)
print('lastCheck ->', now, '| sources:', len(d.get('sources', {})))
