#!/usr/bin/env python3
"""解析 HKMA / InsuranceAsia / IBM / Artemis 日期，列出窗口内候选。"""
import os, re, html

D = os.path.expanduser('~/maoquanqingbao/.cache1029_0030')


def clean(s):
    s = re.sub(r'<[^>]+>', ' ', s or '')
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()


print('=' * 70, '\nHKMA press list')
t = open(f'{D}/hkma_press.raw', encoding='utf-8', errors='replace').read()
rows = re.findall(r'href="(/eng/news-and-media/press-releases/[^"]+)"', t)
print('links:', len(set(rows)))
for r in list(dict.fromkeys(rows))[:20]:
    print('  ', r)

print('=' * 70, '\nHKMA date/near-title context')
for m in re.finditer(r'(20\d\d-\d\d-\d\d|20\d\d/\d\d/\d\d)[^<]{0,40}<[^>]*>\s*(?:<[^>]+>\s*)*([^<]{10,120})', t):
    pass
# 简化：找 date + 后续标题对
chunks = re.split(r'(?=<a )', t)
cnt = 0
for c in chunks:
    m = re.search(r'href="(/eng/news-and-media/press-releases/[^"]+)"', c)
    if not m:
        continue
    txt = clean(c[:1200])
    if len(txt) < 20:
        continue
    print('  ', m.group(1)[:80], '||', txt[:120])
    cnt += 1
    if cnt >= 15:
        break

print('=' * 70, '\nInsuranceAsia list')
t = open(f'{D}/insuranceasia.raw', encoding='utf-8', errors='replace').read()
for m in re.finditer(r'<a[^>]+href="(/insurance/[^"]+)"[^>]*>(.*?)</a>', t, re.S):
    url, tt = m.group(1), clean(m.group(2))
    if len(tt) > 15:
        print('  ', url[:90], '||', tt[:90])

print('=' * 70, '\nIBM Asia list')
t = open(f'{D}/ibm_asia.raw', encoding='utf-8', errors='replace').read()
for m in re.finditer(r'<a[^>]+href="(/asia/news/[^"]+)"[^>]*>(.*?)</a>', t, re.S):
    url, tt = m.group(1), clean(m.group(2))
    if len(tt) > 15:
        print('  ', url[:90], '||', tt[:100])

print('=' * 70, '\nArtemis dates')
t = open(f'{D}/artemis.raw', encoding='utf-8', errors='replace').read()
for m in re.finditer(r'<a[^>]+href="(https://www\.artemis\.bm/news/[^"]+)"[^>]*>(.*?)</a>(.{0,400})', t, re.S):
    url, tt, tail = m.group(1), clean(m.group(2)), clean(m.group(3))
    if len(tt) > 20:
        print('  ', tt[:80], '||', tail[:70])

print('=' * 70, '\nSCMP insurance topic')
t = open(f'{D}/scmp_ins.raw', encoding='utf-8', errors='replace').read()
cnt = 0
for m in re.finditer(r'<a[^>]+href="(https://www\.scmp\.com/[^"]+)"[^>]*>(.*?)</a>', t, re.S):
    url, tt = m.group(1), clean(m.group(2))
    if len(tt) > 25 and '/article/' in url:
        print('  ', tt[:95], '\n      ', url[:120])
        cnt += 1
        if cnt >= 20:
            break
