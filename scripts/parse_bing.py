#!/usr/bin/env python3
"""Parse Bing News RSS: title / pubDate / link / description."""
import re, html, sys

def parse(path):
    raw = open(path, encoding='utf-8', errors='replace').read()
    items = re.findall(r'<item>(.*?)</item>', raw, re.S)
    print(f'== {path} items={len(items)}')
    for it in items:
        t = re.search(r'<title>(.*?)</title>', it, re.S)
        d = re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
        l = re.search(r'<link>(.*?)</link>', it, re.S)
        desc = re.search(r'<description>(.*?)</description>', it, re.S)
        ti = html.unescape(t.group(1)).strip() if t else '?'
        di = d.group(1).strip() if d else '?'
        li = l.group(1).strip() if l else '?'
        de = re.sub(r'<[^>]+>', ' ', html.unescape(desc.group(1))).strip() if desc else ''
        print(f'- [{di}] {ti[:100]}')
        print(f'    URL: {li[:200]}')
        print(f'    DESC: {de[:180]}')

if __name__ == '__main__':
    for p in sys.argv[1:]:
        try:
            parse(p)
        except Exception as e:
            print(f'ERR {p}: {e}')
