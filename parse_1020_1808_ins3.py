import re, os, html
BASE = '/Users/leonliang/maoquanqingbao/.cache1020_1808'
TARGETS = ['prudential.html', 'axa.html', 'sunlife.html', 'iaasia.html']

for fn in TARGETS:
    p = os.path.join(BASE, fn)
    t = open(p, encoding='utf-8', errors='ignore').read()
    t = re.sub(r'<script.*?</script>', ' ', t, flags=re.S | re.I)
    t = re.sub(r'<style.*?</style>', ' ', t, flags=re.S | re.I)
    t = re.sub(r'<[^>]+>', '\n', t)
    lines = [re.sub(r'\s+', ' ', html.unescape(x)).strip() for x in t.split('\n')]
    lines = [x for x in lines if x]
    print('###', fn, 'lines', len(lines))
    hits = 0
    for i, ln in enumerate(lines):
        if re.search(r'(2026|2025)', ln) and len(ln) < 160:
            print('  ', ln[:140])
            hits += 1
            if hits > 40:
                break
    print()
