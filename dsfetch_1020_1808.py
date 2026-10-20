import json, os, urllib.request

key = None
for line in open(os.path.expanduser('~/.hermes/.env'), encoding='utf-8'):
    if line.strip().startswith('DEEPSEEK_API_KEY='):
        key = line.strip().split('=', 1)[1].strip().strip('"').strip("'")
if not key:
    print('NO KEY')
    raise SystemExit(1)

for url in ['https://www.ia.org.hk/en/infocenter/press_releases.html']:
    body = json.dumps({'url': url}).encode()
    req = urllib.request.Request('https://api.deepseek.com/v1/tools/fetch', data=body,
                                 headers={'Authorization': 'Bearer ' + key, 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            js = json.loads(r.read().decode())
        print('OK', url)
        txt = json.dumps(js, ensure_ascii=False)
        print(txt[:3000])
    except Exception as e:
        print('ERR', url, repr(e))
        try:
            print(e.read().decode()[:600])
        except Exception:
            pass
