import re, os, html
BASE = '/Users/leonliang/maoquanqingbao/.cache1020_1808'

TARGETS = ['aia.html', 'prudential.html', 'axa.html', 'sunlife.html', 'iaasia.html', 'manulife.html']

for fn in TARGETS:
    p = os.path.join(BASE, fn)
    if not os.path.exists(p):
        print('###', fn, 'MISSING')
        continue
    t = open(p, encoding='utf-8', errors='ignore').read()
    t = re.sub(r'<script.*?</script>', ' ', t, flags=re.S | re.I)
    t = re.sub(r'<style.*?</style>', ' ', t, flags=re.S | re.I)
    print('###', fn, 'len', len(t))
    # collect (text, href) pairs
    seen = set()
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', t, re.S):
        href, inner = m.group(1), m.group(2)
        txt = re.sub(r'<[^>]+>', ' ', inner)
        txt = re.sub(r'\s+', ' ', html.unescape(txt)).strip()
        if len(txt) < 14:
            continue
        if not re.search(r'2026', txt) and not re.search(r'\d{1,2}[/-]\d{1,2}[/-]?2026', txt):
            # maybe no date in anchor text; keep title only if looks like news
            pass
        key = txt[:80]
        if key in seen:
            continue
        seen.add(key)
        if len(txt) > 20:
            print('  ', txt[:120], '||', href[:110])
    print()
