import re, html, os
from datetime import datetime, timezone, timedelta

D = '/Users/leonliang/maoquanqingbao/.cache1023_0023'
HKT = timezone(timedelta(hours=8))

def txt(p):
    raw = open(os.path.join(D, p), encoding='utf-8', errors='ignore').read()
    t = re.sub(r'(?is)<(script|style|noscript)[^>]*>.*?</\1>', ' ', raw)
    t = re.sub(r'<[^>]+>', '\n', t)
    t = html.unescape(t)
    lines = [re.sub(r'\s+', ' ', l).strip() for l in t.split('\n')]
    return [l for l in lines if l]

for f, kws in [
    ('hkma.html', ['insurance', 'Insur', 'announce', 'circular', 'ban', 'licen']),
    ('sunlife.html', []),
    ('axa.html', []),
    ('aia.html', []),
    ('pru.html', []),
    ('nfra.html', ['保险']),
]:
    print('\n=====', f)
    ls = txt(f)
    print('lines:', len(ls))
    for l in ls[:60]:
        print('   ', l[:160])
