#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, html
D = '/Users/leonliang/maoquanqingbao/data/_1017_0048/'
def strip(t):
    t = re.sub(r'<[^>]+>', ' ', t or '')
    return html.unescape(re.sub(r'\s+', ' ', t)).strip()

r = open(D + 'axa2026.out', encoding='utf-8', errors='replace').read()
print('=== AXA blocks ===')
for m in re.finditer(r'(20\d{2}\s*年\s*\d{1,2}\s*月\s*\d{1,2}\s*日|\d{4}-\d{2}-\d{2})', strip(r)):
    seg = strip(r)[m.start():m.start()+260]
    print(' >', seg[:250])
    print('   ---')
