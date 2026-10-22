import json, urllib.request
from pathlib import Path

ENV = Path.home() / '.hermes' / '.env'
key = [l.split('=', 1)[1].strip().strip('"').strip("'") for l in ENV.read_text().splitlines()
       if l.strip().startswith('DEEPSEEK_API_KEY')][0]
D = Path('/Users/leonliang/maoquanqingbao/.cache1023_0023')
D.mkdir(parents=True, exist_ok=True)

for name, u in {
    'ia_press_ds': 'https://www.ia.org.hk/en/infocenter/press_releases/',
    'ia_circ_ds': 'https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html',
    'ia_whatsnew_ds': 'https://www.ia.org.hk/en/infocenter/whats_new.html',
    'rn_ds': 'https://www.reinsurancene.ws/',
}.items():
    body = json.dumps({'url': u}).encode()
    req = urllib.request.Request('https://api.deepseek.com/v1/tools/fetch', data=body,
                                 headers={'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            j = json.load(r)
        c = str(j.get('content') or j.get('data', {}).get('content') or '')
        (D / f'{name}.txt').write_text(c, encoding='utf-8')
        print('===', name, len(c), 'chars')
        for line in c.splitlines()[:45]:
            s = line.strip()
            if s:
                print('   ', s[:200])
    except Exception as e:
        print('ERR', name, repr(e)[:200])
