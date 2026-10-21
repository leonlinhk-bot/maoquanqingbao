import json, urllib.request, urllib.error
from pathlib import Path
ENV = Path.home() / '.hermes' / '.env'
key = [l.split('=', 1)[1].strip().strip('"').strip("'") for l in ENV.read_text().splitlines()
       if l.strip().startswith('DEEPSEEK_API_KEY')][0]

urls = [
    'https://www.ia.org.hk/en/infocenter/press_releases.html',
    'https://www.ia.org.hk/en/infocenter/press_releases/',
    'https://www.ia.org.hk/en/infocenter/whats_new.html',
]
for u in urls:
    body = json.dumps({'url': u}).encode()
    req = urllib.request.Request('https://api.deepseek.com/v1/tools/fetch', data=body,
                                 headers={'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            raw = r.read().decode('utf-8', 'ignore')
        print('OK', u, len(raw))
        print(raw[:1500])
    except urllib.error.HTTPError as e:
        print('HTTPERR', u, e.code, e.read().decode('utf-8', 'ignore')[:500])
    except Exception as e:
        print('ERR', u, repr(e)[:200])
    print('-' * 60)
