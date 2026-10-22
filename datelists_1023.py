import re, html, os

D = '/Users/leonliang/maoquanqingbao/.cache1023_0023'

def lines(p):
    raw = open(os.path.join(D, p), encoding='utf-8', errors='ignore').read()
    t = re.sub(r'(?is)<(script|style|noscript)[^>]*>.*?</\1>', ' ', raw)
    t = re.sub(r'<[^>]+>', '\n', t)
    t = html.unescape(t)
    return [re.sub(r'\s+', ' ', l).strip() for l in t.split('\n') if l.strip()]

for f in ['hkma.html', 'sunlife.html', 'aia.html', 'pru.html', 'manulife.html', 'nfra.html', 'hkfi.html']:
    ls = lines(f)
    hits = [(i, l) for i, l in enumerate(ls)
            if re.match(r'^(2026|2025)[-年./]?\s?\d{1,2}[-月./]\s?\d{1,2}', l) or re.match(r'^\d{1,2} \w+ 2026', l)]
    print(f'\n===== {f}  hits {len(hits)}')
    for i, l in hits[:25]:
        ctx = ' / '.join(ls[i+1:i+3])[:160]
        print(f'  {l[:40]}  ||  {ctx}')
