import json, subprocess, datetime

NOW = subprocess.run(["date", "+%Y-%m-%dT%H:%M:%S+08:00"], capture_output=True, text=True).stdout.strip()
p = 'data/last-check.json'
d = json.load(open(p, encoding='utf-8'))
d['lastCheck'] = NOW
for k, v in d.get('sources', {}).items():
    v['last'] = NOW
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('lastCheck =', NOW, '| sources updated:', len(d.get('sources', {})))
