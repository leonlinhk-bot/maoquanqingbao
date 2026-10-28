import json, re, os
base = '/Users/leonliang/maoquanqingbao'
d = json.load(open(os.path.join(base, 'data/live-items.json')))
print('live-items count:', len(d['items']))
app = open(os.path.join(base, 'app.js')).read()
m = re.search(r'const DATA\s*=\s*(\[.*?\]);', app, re.S)
print('app.js DATA array found:', bool(m))
if m:
    try:
        arr = json.loads(m.group(1))
        print('app.js DATA count:', len(arr))
        print('app.js first id:', arr[0].get('id'))
    except Exception as e:
        print('parse err', e)
core_path = os.path.join(base, 'data/core.json')
if os.path.exists(core_path):
    c = json.load(open(core_path))
    print('core stats:', json.dumps(c.get('stats', {}), ensure_ascii=False)[:300])
    print('core generatedAt:', c.get('generatedAt'))
else:
    print('no core.json')
print('--- new items on 2026-10-28 ---')
for i in d['items']:
    if i['publishedAt'][:10] == '2026-10-28':
        print(i['publishedAt'], '|', i.get('sourceKey'), '|', i.get('verifyStatus'), '|', i['title']['sc'][:55])
