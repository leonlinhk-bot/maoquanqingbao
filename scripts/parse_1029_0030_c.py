#!/usr/bin/env python3
import os, re, html

D = os.path.expanduser('~/maoquanqingbao/.cache1029_0030')


def clean(s):
    s = re.sub(r'<[^>]+>', ' ', s or '')
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()


print('=== INSURANCEASIA: all /insurance/ hrefs ===')
t = open(f'{D}/insuranceasia.raw', encoding='utf-8', errors='replace').read()
u = sorted(set(re.findall(r'href="([^"]*/insurance/[^"]*)"', t)))
print(len(u))
for x in u[:40]:
    print('  ', x)

print()
print('=== INSURANCEASIA: title-ish h2/h3 ===')
for m in list(re.finditer(r'<h[234][^>]*>(.*?)</h[234]>', t, re.S))[:40]:
    c = clean(m.group(1))
    if len(c) > 20:
        print('  ', c[:110])

print()
print('=== SCMP: article links ===')
s = open(f'{D}/scmp_ins.raw', encoding='utf-8', errors='replace').read()
arts = sorted(set(re.findall(r'(https://www\.scmp\.com/[a-z\-]+/article/\d+/[^"\s\\]+)', s)))
print('count', len(arts))
for a in arts[:25]:
    print('  ', a)
print()
print('=== SCMP: titles near articles ===')
for m in list(re.finditer(r'<a[^>]+href="(https://www\.scmp\.com/[^"]*article[^"]*)"[^>]*>(.*?)</a>', s, re.S))[:25]:
    print('  ', clean(m.group(2))[:95], '||', m.group(1)[:110])
