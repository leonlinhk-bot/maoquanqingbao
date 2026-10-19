import json, os, urllib.request, time
from pathlib import Path
ENV = Path.home() / '.hermes' / '.env'
key, base = None, 'https://api.deepseek.com'
for line in ENV.read_text().splitlines():
    if line.startswith('DEEPSEEK_API_KEY='):
        key = line.split('=', 1)[1].strip().strip('"').strip("'")
    elif line.startswith('DEEPSEEK_BASE_URL='):
        base = line.split('=', 1)[1].strip().strip('"').strip("'").rstrip('/')

def fetch(url, out):
    req = urllib.request.Request(base + '/v1/tools/fetch', data=json.dumps({'url': url}).encode(),
        headers={'Authorization': 'Bearer ' + key, 'Content-Type': 'application/json'}, method='POST')
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                j = json.loads(r.read().decode())
            c = j.get('content') or ''
            open(out, 'w', encoding='utf-8').write(c)
            print('OK', url, '->', out, len(c))
            return c
        except Exception as e:
            print('retry', attempt, type(e).__name__, e)
            time.sleep(5)
    return ''

if __name__ == '__main__':
    import sys
    fetch(sys.argv[1], sys.argv[2])
