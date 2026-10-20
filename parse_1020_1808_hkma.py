import re, os, html
from datetime import datetime, timezone, timedelta
HKT = timezone(timedelta(hours=8))
BASE = '/Users/leonliang/maoquanqingbao/.cache1020_1808'


def text(p):
    if not os.path.exists(p):
        return ''
    t = open(p, encoding='utf-8', errors='ignore').read()
    t = re.sub(r'<script.*?</script>', ' ', t, flags=re.S | re.I)
    t = re.sub(r'<style.*?</style>', ' ', t, flags=re.S | re.I)
    t = re.sub(r'<[^>]+>', '\n', t)
    t = html.unescape(t)
    lines = [re.sub(r'\s+', ' ', x).strip() for x in t.split('\n')]
    return '\n'.join([x for x in lines if x])


for fn in ['hkma.html']:
    print('#####', fn)
    t = text(os.path.join(BASE, fn))
    # find lines with dates in 2026-10
    for i, ln in enumerate(t.split('\n')):
        if re.search(r'(1[5-9]|20) October 2026|2026-10-1[5-9]|2026-10-20', ln):
            print(i, '|', ln[:150])
