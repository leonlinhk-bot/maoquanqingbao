#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, html

def clean(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S)
    s = re.sub(r'<style.*?</style>', ' ', s, flags=re.S)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()

# --- SCMP: links whose URL contains 2026/08 ---
h = open('/tmp/src/scmp.html', encoding='utf-8').read()
print('== SCMP /2026/08 links')
seen = set()
cnt = 0
for m in re.finditer(r'<a[^>]*href="([^"]*2026/08[^"]*)"[^>]*>(.*?)</a>', h, re.S):
    u, t = m.group(1), clean(m.group(2))
    if not t or len(t) < 15 or (u, t) in seen:
        continue
    seen.add((u, t))
    print('  -', t[:105], '|', u[:110])
    cnt += 1
    if cnt >= 15:
        break
print(f'  [total {cnt}]')

# --- SunLife: dates near 2026 links ---
h = open('/tmp/src/sunlife.html', encoding='utf-8').read()
print('== SunLife 2026 items with dates')
for m in re.finditer(r'<a[^>]*href="(/en/about-us/newsroom/news-releases/2026/[^"]+)"[^>]*>(.*?)</a>', h, re.S):
    u, t = m.group(1), clean(m.group(2))
    if not t:
        continue
    # look back 400 chars for a date
    back = h[max(0, m.start() - 500):m.start()]
    d = re.findall(r'(\d{1,2}\s+\w{3,9}\s+2026|\w{3,9}\s+\d{1,2},?\s+2026|\d{4}-\d{2}-\d{2})', back)
    print('  -', (d[-1] if d else '?'), '|', t[:90], '|', u[:90])
