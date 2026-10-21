import json, urllib.request, urllib.error, re
from pathlib import Path
ENV = Path.home() / '.hermes' / '.env'
key = [l.split('=', 1)[1].strip().strip('"').strip("'") for l in ENV.read_text().splitlines()
       if l.strip().startswith('DEEPSEEK_API_KEY')][0]
D = Path('/Users/leonliang/maoquanqingbao/data/_1022_0037')

urls = {
 'circ_reg': 'https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters.html',
 'circ_2026': 'https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html',
 'circ_aml': 'https://www.ia.org.hk/en/legislative_framework/circulars/aml.html',
}
for name, u in urls.items():
    body = json.dumps({'url': u}).encode()
    req = urllib.request.Request('https://api.deepseek.com/v1/tools/fetch', data=body,
                                 headers={'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            j = json.loads(r.read().decode('utf-8', 'ignore'))
        c = j.get('content', '')
        (D / f'{name}.txt').write_text(c, encoding='utf-8')
        print(f'=== {name}: {len(c)} chars')
        # print lines that look like dates or titles
        lines = [l.strip() for l in c.splitlines() if l.strip()]
        for l in lines:
            if re.search(r'(2026|2025)', l) or 'ircular' in l:
                print('   ', l[:200])
    except urllib.error.HTTPError as e:
        print('HTTPERR', name, e.code, e.read().decode()[:200])
    except Exception as e:
        print('ERR', name, repr(e)[:150])
    print('-'*50)
