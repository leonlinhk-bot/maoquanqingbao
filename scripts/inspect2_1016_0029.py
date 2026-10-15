#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, html, json
D = '/Users/leonliang/maoquanqingbao/data/_1016_0029/'

def clean(t):
    t = re.sub(r'<[^>]+>', ' ', t or '')
    return html.unescape(re.sub(r'\s+', ' ', t)).strip()

raw = open(D + 'hkma.out', encoding='utf-8', errors='replace').read()
print('=== HKMA block around 20261015-4 ===')
i = raw.find('20261015-4')
print(clean(raw[max(0, i-1200):i+400])[-900:])
print()
print('=== HKMA date headers (all) ===')
for m in re.finditer(r'class="[^"]*date[^"]*"[^>]*>(.*?)<', raw, re.S):
    print(' ', clean(m.group(1))[:40])
print()
print('=== govhk insurance-related in window ===')
g = open(D + 'govhk.out', encoding='utf-8', errors='replace').read()
for e in re.findall(r'<item[\s>].*?</item>', g, re.S):
    ti = clean(re.search(r'<title[^>]*>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', e, re.S).group(1))
    pu = re.search(r'<pubDate[^>]*>(.*?)</', e, re.S)
    if re.search(r'保險|保監|理賠|強積金|退休|年金|財富|資產管理|家族|基金|金融|保險業|再保', ti):
        print('  ', clean(pu.group(1)) if pu else '?', '|', ti[:100])
print()
print('=== IBM titles top 12 ===')
b = open(D + 'ibm.out', encoding='utf-8', errors='replace').read()
for e in re.findall(r'<item[\s>].*?</item>', b, re.S)[:12]:
    ti = clean(re.search(r'<title[^>]*>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', e, re.S).group(1))
    pu = re.search(r'<pubDate[^>]*>(.*?)</', e, re.S)
    ln = re.search(r'<link[^>]*>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</link>', e, re.S)
    print('  ', (clean(pu.group(1)) if pu else '?')[:31], '|', ti[:90])
    print('      ', (clean(ln.group(1)) if ln else '')[:120])
