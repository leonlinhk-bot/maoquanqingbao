#!/usr/bin/env python3
"""Print full RSS descriptions for target govhk + IBM items from already-fetched raw files."""
import re, html

def blocks(raw, tag):
    return re.findall(rf'<{tag}\b.*?</{tag}>', raw, re.S)

def g(blk, tag):
    m = re.search(rf'<{tag}[^>]*>(.*?)</{tag}>', blk, re.S)
    return m.group(1) if m else ''

def txt(t):
    t = re.sub(r'(?s)<!\[CDATA\[(.*?)\]\]>', r'\1', t)
    t = re.sub(r'<br\s*/?>', '\n', t)
    t = re.sub(r'</p>', '\n', t)
    t = re.sub(r'<[^>]+>', ' ', t)
    return re.sub(r'[ \t\u00a0\u3000]+', ' ', html.unescape(t)).strip()

gov = open('data/_1014/govhk.raw', encoding='utf-8').read()
TARGETS = ['P2026101400351', 'P2026101300384', 'P2026101300435', 'P2026101300469', 'P2026101400250']
for blk in blocks(gov, 'item'):
    lk = g(blk, 'link')
    if any(t in lk for t in TARGETS):
        print('\n=========', lk)
        print('TITLE:', txt(g(blk, 'title')))
        print('DATE:', g(blk, 'pubDate'))
        print(txt(g(blk, 'description'))[:2200])

ibm = open('data/_1014/insurancebusinessmag.raw', encoding='utf-8').read()
print('\n\n########## IBM Atom entries ##########')
for blk in blocks(ibm, 'entry'):
    ti = txt(g(blk, 'title'))
    if any(k in ti for k in ('Manulife launches enterprise AI', 'Indonesia', 'Moody', 'Lloyd')):
        print('\n===', g(blk, 'updated') or g(blk, 'published'), '|', ti)
        lm = re.search(r'<link[^>]*href="([^"]+)"', blk)
        print('LINK:', lm.group(1) if lm else '')
        print(txt(g(blk, 'summary') or g(blk, 'content'))[:1600])
