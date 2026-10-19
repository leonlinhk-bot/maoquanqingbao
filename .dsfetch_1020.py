import json, os, sys, urllib.request, time
from pathlib import Path

ENV = Path.home() / '.hermes' / '.env'
key, base = None, 'https://api.deepseek.com'
if ENV.is_file():
    for line in ENV.read_text().splitlines():
        if line.startswith('DEEPSEEK_API_KEY='):
            key = line.split('=', 1)[1].strip().strip('"').strip("'")
        elif line.startswith('DEEPSEEK_BASE_URL='):
            base = line.split('=', 1)[1].strip().strip('"').strip("'").rstrip('/')
key = key or os.environ.get('DEEPSEEK_API_KEY')
print('key?', bool(key), 'base', base)

def fetch(url):
    payload = {'url': url}
    req = urllib.request.Request(base + '/v1/tools/fetch',
        data=json.dumps(payload).encode(),
        headers={'Authorization': 'Bearer ' + key, 'Content-Type': 'application/json'}, method='POST')
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            j = json.loads(r.read().decode())
        print('== FETCH', url, 'took %.1fs' % (time.time() - t0))
        print(json.dumps(j, ensure_ascii=False)[:400])
        return j
    except Exception as e:
        print('== FAIL', url, type(e).__name__, e, 'after %.1fs' % (time.time() - t0))
        return None

if __name__ == '__main__':
    for u in sys.argv[1:]:
        j = fetch(u)
        if j:
            c = j.get('content') or j.get('text') or ''
            if isinstance(c, dict):
                c = json.dumps(c, ensure_ascii=False)
            print('--- content len', len(c))
            print(c[:4000])
        print()
