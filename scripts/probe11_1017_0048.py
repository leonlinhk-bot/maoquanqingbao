#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, html
D = '/Users/leonliang/maoquanqingbao/data/_1017_0048/'
def strip(t):
    t = re.sub(r'<[^>]+>', ' ', t or '')
    return html.unescape(re.sub(r'\s+', ' ', t)).strip()
r = open(D + 'hkfi2.out', encoding='utf-8', errors='replace').read()
txt = strip(r)
print('dates:', sorted(set(re.findall(r'\d{1,2}\s+\w+\s+202[56]', txt)))[:20])
print('iso:', sorted(set(re.findall(r'202[56]-\d{2}-\d{2}', txt)))[:20])
for m in re.findall(r'href="([^"]*(?:media|release|news)[^"]*)"[^>]*>([^<]{8,120})<', r)[:20]:
    print('L', m[0][:110], '|', strip(m[1])[:80])
print('--- kill-shot: search 2026 dates near titles ---')
for m in re.finditer(r'(2026[^ ]{0,12})', txt):
    print(' >', txt[max(0, m.start()-90):m.start()+90])
    break
