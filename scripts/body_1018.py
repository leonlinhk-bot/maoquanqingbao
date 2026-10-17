import re, html, os, sys
C = '/Users/leonliang/maoquanqingbao/.cache1018_0012'

def text(fn, limit=3000):
    raw = open(os.path.join(C, fn), encoding='utf-8', errors='ignore').read()
    raw = re.sub(r'<script.*?</script>', ' ', raw, flags=re.S | re.I)
    raw = re.sub(r'<style.*?</style>', ' ', raw, flags=re.S | re.I)
    t = re.sub(r'<[^>]+>', '\n', raw)
    t = html.unescape(t)
    lines = [re.sub(r'\s+', ' ', x).strip() for x in t.split('\n')]
    lines = [x for x in lines if len(x) > 45]
    out = []
    seen = set()
    for x in lines:
        if x in seen:
            continue
        seen.add(x)
        out.append(x)
    print('#####', fn)
    body = '\n'.join(out)
    print(body[:limit])
    print()

for fn in sys.argv[1:]:
    text(fn)
