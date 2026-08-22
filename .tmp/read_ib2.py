import re, html

def strip_tags(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

def paragraphs(path, maxp=8):
    raw = open(path, encoding='utf-8', errors='ignore').read()
    ps = re.findall(r'<p[^>]*>(.*?)</p>', raw, re.S | re.I)
    out = []
    for p in ps:
        t = strip_tags(p)
        if len(t) > 40 and not t.startswith('{'):
            out.append(t)
    return out[:maxp]

for fn in ['ib-aia-broker.html', 'ib-etf-mainland.html', 'ib-pingan.html']:
    print('=' * 25, fn)
    for p in paragraphs('data/_raw/t0822c/' + fn):
        print('  -', p[:250])
    print()
