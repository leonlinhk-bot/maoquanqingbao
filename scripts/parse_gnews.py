#!/usr/bin/env python3
"""Parse Google News RSS XML: title / pubDate / source / link."""
import re, html, sys

def parse(path):
    raw = open(path, encoding='utf-8', errors='replace').read()
    items = re.findall(r'<item>(.*?)</item>', raw, re.S)
    print(f'== {path} items={len(items)}')
    for it in items:
        t = re.search(r'<title>(.*?)</title>', it, re.S)
        d = re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
        s = re.search(r'<source[^>]*>(.*?)</source>', it, re.S)
        l = re.search(r'<link>(.*?)</link>', it, re.S)
        ti = html.unescape(t.group(1)).strip() if t else '?'
        di = d.group(1).strip() if d else '?'
        si = html.unescape(s.group(1)).strip() if s else '?'
        li = l.group(1).strip() if l else '?'
        print(f'- [{di}] ({si}) {ti[:110]}')
        print(f'    {li[:160]}')

if __name__ == '__main__':
    for p in sys.argv[1:]:
        try:
            parse(p)
        except Exception as e:
            print(f'ERR {p}: {e}')
