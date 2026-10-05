import re, html, json, os
C = 'data/_cache1006_0156'
def clean(s):
    return html.unescape(re.sub(r'<[^>]+>', '', s or '')).strip()

for f in ['ibm_conduct.html', 'ibm_mas.html']:
    p = os.path.join(C, f)
    if not os.path.exists(p):
        print('MISSING', f); continue
    h = open(p, encoding='utf-8', errors='ignore').read()
    print('=' * 66)
    print(f)
    for pat in [r'"datePublished"\s*:\s*"([^"]+)"', r'"dateModified"\s*:\s*"([^"]+)"',
                r'property="article:published_time"\s+content="([^"]+)"',
                r'(?:Published|Published on|date)\D{0,20}(\d{1,2}\s+\w{3,9}\s+2026|\w+\s+\d{1,2},\s+2026)']:
        m = re.findall(pat, h)
        if m:
            print('  ', pat[:40], '->', m[:4])
    t = re.search(r'<title>(.*?)</title>', h, re.S)
    print('   title:', clean(t.group(1))[:100] if t else '')
    d = re.findall(r'\b\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\w*\s+2026\b', h)
    print('   date tokens:', sorted(set(d))[:10])

db = json.load(open('data/live-items.json'))
print('=' * 66)
for key in ['artemis', 'sunlife', 'axa', 'prudential', 'aia', 'manulife', 'hkma', 'govhk', 'family_office', 'insurtech', 'scmp', 'nfra']:
    ids = sorted(x['id'] for x in db['items'] if x.get('sourceKey') == key)
    print('---', key, len(ids))
    print('   ', ' | '.join(ids[-8:]))
