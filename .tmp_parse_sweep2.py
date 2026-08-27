#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, html

def clean(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S)
    s = re.sub(r'<style.*?</style>', ' ', s, flags=re.S)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()

def links_with_text(h):
    out = []
    for m in re.finditer(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', h, re.S):
        u, t = m.group(1), clean(m.group(2))
        if t and len(t) > 12:
            out.append((u, t))
    return out

for name in ['aia', 'prudential', 'axa', 'sunlife', 'scmp']:
    h = open(f'/tmp/src/{name}.html', encoding='utf-8').read()
    print(f'== {name}')
    seen = set()
    cnt = 0
    for u, t in links_with_text(h):
        if '2026' in (t + u):
            key = t
            if key in seen:
                continue
            seen.add(key)
            print('  -', t[:110], '|', u[:120])
            cnt += 1
            if cnt >= 20:
                break
    print(f'  [total {cnt}]')
