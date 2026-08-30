#!/usr/bin/env python3
"""Parse InsuranceAsia RSS and HKMA press-release HTML; print items with dates."""
import re, html, sys
from datetime import datetime

def parse_iaasia(path):
    raw = open(path, encoding='utf-8', errors='replace').read()
    items = re.findall(r'<item>(.*?)</item>', raw, re.S)
    print(f'[InsuranceAsia] items: {len(items)}')
    for it in items[:20]:
        t = re.search(r'<title>(.*?)</title>', it, re.S)
        l = re.search(r'<link>(.*?)</link>', it, re.S)
        d = re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
        ti = html.unescape(t.group(1)).strip() if t else '?'
        li = l.group(1).strip() if l else '?'
        di = d.group(1).strip() if d else '?'
        print(f'- {ti[:110]} | {di} | {li[:90]}')

def parse_hkma(path):
    raw = open(path, encoding='utf-8', errors='replace').read()
    # HKMA press release items: look for links containing press release ids + dates
    links = re.findall(r'<a[^>]+href="([^"]*press[^"]*)"[^>]*>(.*?)</a>', raw, re.S)
    seen = set()
    print(f'[HKMA] candidate links: {len(links)}')
    for href, text in links:
        txt = re.sub(r'<[^>]+>', '', text)
        txt = html.unescape(txt).strip()
        if not txt or href in seen:
            continue
        seen.add(href)
        print(f'- {txt[:110]} | {href[:110]}')

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'ia':
        parse_iaasia('/tmp/iaasia.xml')
    elif len(sys.argv) > 1 and sys.argv[1] == 'hkma':
        parse_hkma('/tmp/hkma.html')
