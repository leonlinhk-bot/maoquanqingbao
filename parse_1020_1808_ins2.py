import re, os, html
BASE = '/Users/leonliang/maoquanqingbao/.cache1020_1808'
TARGETS = ['prudential.html', 'axa.html', 'sunlife.html', 'iaasia.html', 'manulife.html']

for fn in TARGETS:
    p = os.path.join(BASE, fn)
    if not os.path.exists(p):
        print('###', fn, 'MISSING')
        continue
    t = open(p, encoding='utf-8', errors='ignore').read()
    t = re.sub(r'<script.*?</script>', ' ', t, flags=re.S | re.I)
    t = re.sub(r'<style.*?</style>', ' ', t, flags=re.S | re.I)
    print('###', fn, 'len', len(t))
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', t, re.S):
        href, inner = m.group(1), m.group(2)
        txt = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', inner))).strip()
        if len(txt) < 18:
            continue
        if re.search(r'2026年10月|October 2026|10/2026|2026-10', txt, re.I):
            print('  *', txt[:130], '||', href[:100])
    print()
