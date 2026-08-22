import re, html

def strip_tags(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

def paragraphs(path, maxp=6):
    raw = open(path, encoding='utf-8', errors='ignore').read()
    ps = re.findall(r'<p[^>]*>(.*?)</p>', raw, re.S | re.I)
    out = []
    for p in ps:
        t = strip_tags(p)
        if len(t) > 30 and not t.startswith('{'):
            out.append(t)
    return out[:maxp]

for fn in ['hkma-pboC-bills.html', 'hkma-scam-banks-0820.html']:
    print('=' * 25, fn)
    for p in paragraphs('data/_raw/t0822c/' + fn):
        print('  -', p[:300])
    print()
