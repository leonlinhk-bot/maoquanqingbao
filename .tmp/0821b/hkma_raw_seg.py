#!/usr/bin/env python3
import re, html

raw = open('.tmp/0821b/hkma_0821_3.html', encoding='utf-8', errors='ignore').read()
for m in re.finditer(r'Renminbi Bills', raw):
    s = max(0, m.start() - 300)
    seg = raw[s:m.start() + 4000]
    seg = re.sub(r'<[^>]+>', ' ', seg)
    seg = html.unescape(re.sub(r'\s+', ' ', seg))
    print(seg[:3000])
    print('-----')
    break

raw2 = open('.tmp/0821b/hkma_0820_4.html', encoding='utf-8', errors='ignore').read()
for m in re.finditer(r'Scam alert related to banks', raw2):
    s = max(0, m.start() - 300)
    seg = raw2[s:m.start() + 4000]
    seg = re.sub(r'<[^>]+>', ' ', seg)
    seg = html.unescape(re.sub(r'\s+', ' ', seg))
    print(seg[:2500])
    print('=====')
    break
