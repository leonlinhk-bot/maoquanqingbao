#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract article title + body text from fetched article HTML (Next.js pages)."""
import re, json, sys, html as H
from html.parser import HTMLParser

def get_title(html):
    m = re.search(r'<title>([^<]*)</title>', html)
    t = re.search(r'<meta[^>]+property="og:title"[^>]+content="([^"]*)"', html)
    h = re.search(r'"headline":"([^"]*)"', html)
    return (t.group(1) if t else (h.group(1) if h else (m.group(1) if m else '?'))).strip()

def get_date(html):
    for pat in (r'"datePublished":"([^"]*)"', r'<meta[^>]+property="article:published_time"[^>]+content="([^"]*)"', r'"dateModified":"([^"]*)"'):
        m = re.search(pat, html)
        if m:
            return m.group(1)
    return '?'

class TextExtract(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.skip = 0
        self.in_script = False
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style', 'noscript', 'svg', 'head'):
            self.skip += 1
        if tag in ('p', 'div', 'br', 'h1', 'h2', 'h3', 'li'):
            self.parts.append('\n')
    def handle_endtag(self, tag):
        if tag in ('script', 'style', 'noscript', 'svg', 'head') and self.skip > 0:
            self.skip -= 1
    def handle_data(self, data):
        if self.skip == 0:
            self.parts.append(data)

def body_text(html):
    p = TextExtract()
    p.feed(html)
    txt = re.sub(r'\n{2,}', '\n', ''.join(p.parts))
    lines = [H.unescape(l.strip()) for l in txt.split('\n')]
    lines = [l for l in lines if l and len(l) > 2]
    return lines

for path in sys.argv[1:]:
    html = open(path, encoding='utf-8', errors='replace').read()
    print(f'\n########## {path}')
    print('TITLE:', get_title(html)[:120])
    print('DATE :', get_date(html))
    lines = body_text(html)
    # find start of content: first line containing headline keywords or long line
    shown = 0
    for l in lines:
        if len(l) > 60 or (len(l) > 30 and shown == 0):
            print('  ', l[:200])
            shown += 1
        if shown > 22:
            break
