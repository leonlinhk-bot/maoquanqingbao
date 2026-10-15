#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, html
D = '/Users/leonliang/maoquanqingbao/data/_1016_0029/'

def txt(p):
    raw = open(D + p, encoding='utf-8', errors='replace').read()
    return raw

# HKMA press release page: find date headers + titles
raw = txt('hkma.out')
print('=== HKMA ===')
for m in re.finditer(r'<a[^>]+href="(/eng/news-and-media/press-releases/[^"]+)"[^>]*>(.*?)</a>', raw, re.S):
    t = re.sub(r'<[^>]+>', ' ', m.group(2))
    t = html.unescape(re.sub(r'\s+', ' ', t)).strip()
    if len(t) > 25:
        print(' ', m.group(1)[:90], '|', t[:110])
print('--- date strings present ---')
for m in re.finditer(r'(1[0-9]|2[0-9]|3[01]) (?:Oct|October) 2026', raw):
    pass
dates = re.findall(r'\d{1,2} October 2026', raw)[:15]
print(dates)
