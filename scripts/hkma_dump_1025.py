#!/usr/bin/env python3
import re, html, glob, os
p = 'data/_raw_1025_0044/hkma_press_0045.html'
b = open(p, 'rb').read().decode('utf-8', 'ignore')
b2 = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', b, flags=re.S | re.I)
t = html.unescape(re.sub(r'<[^>]+>', '\n', b2))
lines = [re.sub(r'\s+', ' ', x).strip() for x in t.split('\n')]
lines = [x for x in lines if x]
print('total lines', len(lines))
idx = [n for n, x in enumerate(lines) if re.search(r'2026|Oct', x)]
print('lines mentioning 2026/Oct:', len(idx))
for n in idx[:30]:
    print(n, '|', lines[n][:170])
print('---- tail 60')
for n in range(max(0, len(lines) - 60), len(lines)):
    print(n, '|', lines[n][:170])
