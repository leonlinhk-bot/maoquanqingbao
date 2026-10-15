#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, html
D = '/Users/leonliang/maoquanqingbao/data/_1016_0029/'

def clean(t):
    t = re.sub(r'<[^>]+>', ' ', t or '')
    return html.unescape(re.sub(r'\s+', ' ', t)).strip()

print('=== HKFI (media-centre) ===')
raw = open(D + 'hkfi.out', encoding='utf-8', errors='replace').read()
for m in re.finditer(r'href="([^"]*(?:press|media|release|news)[^"]*)"[^>]*>(.*?)</a>', raw, re.S | re.I):
    t = clean(m.group(2))
    if 20 < len(t) < 200:
        print(' ', m.group(1)[:80], '|', t[:110])

print()
print('=== SCMP rss dates (top 15) ===')
s = open(D + 'scmp.out', encoding='utf-8', errors='replace').read()
for e in re.findall(r'<item[\s>].*?</item>', s, re.S)[:15]:
    ti = re.search(r'<title[^>]*>(.*?)</title>', e, re.S)
    pu = re.search(r'<pubDate[^>]*>(.*?)</', e, re.S)
    print('  ', clean(pu.group(1)) if pu else '?', '|', clean(ti.group(1))[:85] if ti else '')

print()
print('=== IBM titles top 14 ===')
b = open(D + 'ibm.out', encoding='utf-8', errors='replace').read()
for e in re.findall(r'<item[\s>].*?</item>', b, re.S)[:14]:
    ti = re.search(r'<title[^>]*>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', e, re.S)
    pu = re.search(r'<pubDate[^>]*>(.*?)</', e, re.S)
    ln = re.search(r'<link[^>]*>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</link>', e, re.S)
    print('  ', clean(pu.group(1)) if pu else '?', '|', clean(ti.group(1))[:85] if ti else '')
    print('      ', clean(ln.group(1))[:110] if ln else '')
