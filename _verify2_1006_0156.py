import json, subprocess, datetime, time, os
for f in ['feed/all.json', 'feed/featured.json', 'data/items.json', 'app.js']:
    if os.path.exists(f):
        print(f, os.path.getsize(f), 'bytes', end=' ')
        if f.endswith('.json'):
            d = json.load(open(f))
            print('| itemCount', d.get('itemCount'), '| generatedAt', d.get('generatedAt'))
        else:
            print('| contains PK', 'HKII_VER' in open(f).read())
    else:
        print(f, 'MISSING')

print('--- live index.html data path ---')
h = open('index.html', encoding='utf-8').read()
import re
for m in re.finditer(r'(fetch\(|src=|HKII_\w+Promise|\.json)', h):
    pass
print([l.strip()[:120] for l in h.splitlines() if 'json' in l or 'app.js' in l][:10])

print('--- deployed recheck ---')
for i in range(6):
    time.sleep(20)
    out = subprocess.run(['curl', '-sL', '-m', '25',
                          'https://hkmaoquanqingbao.com/feed/all.json?cb=' + str(int(time.time()))],
                         capture_output=True, text=True).stdout
    try:
        d = json.loads(out)
        n = d.get('itemCount')
        print('try', i + 1, 'itemCount', n, 'generatedAt', d.get('generatedAt'))
        if n and n >= 1168:
            break
    except Exception as e:
        print('try', i + 1, 'parse fail', out[:100])
