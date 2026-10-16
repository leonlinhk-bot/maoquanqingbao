#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, html
D = '/Users/leonliang/maoquanqingbao/data/_1017_0048/'
def strip(t):
    t = re.sub(r'<[^>]+>', ' ', t or '')
    return html.unescape(re.sub(r'\s+', ' ', t)).strip()
raw = open(D + 'ibm.out', encoding='utf-8', errors='replace').read()
print('head:', raw[:300].replace('\n', ' '))
ents = re.findall(r'<entry[\s>].*?</entry>', raw, re.S)
print('entries', len(ents))
for e in ents[:6]:
    t = re.search(r'<title[^>]*>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', e, re.S)
    l = re.search(r'<link[^>]*href="([^"]+)"', e)
    if not l:
        l = re.search(r'<link[^>]*>(.*?)</link>', e, re.S)
    d = re.search(r'<(?:updated|published)[^>]*>(.*?)</', e, re.S)
    s = re.search(r'<(?:summary|content)[^>]*>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</(?:summary|content)>', e, re.S)
    print('-', strip(t.group(1) if t else '')[:90])
    print('   U', (l.group(1) if l else '')[:140])
    print('   D', strip(d.group(1)) if d else '')
    print('   S', strip(s.group(1) if s else '')[:500])
