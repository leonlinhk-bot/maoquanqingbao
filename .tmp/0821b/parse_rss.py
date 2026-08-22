#!/usr/bin/env python3
import re, html, json, sys, glob

def parse_rss(path):
    txt = open(path, encoding='utf-8', errors='ignore').read()
    items = re.findall(r'<item>(.*?)</item>', txt, re.S)
    out = []
    for it in items:
        def g(tag):
            m = re.search(r'<%s[^>]*>(.*?)</%s>' % (tag, tag), it, re.S)
            return html.unescape(m.group(1)).strip() if m else ''
        out.append({'title': g('title'), 'link': g('link'), 'pubDate': g('pubDate'), 'desc': g('description')[:300]})
    return out

def parse_ia(path):
    txt = open(path, encoding='utf-8', errors='ignore').read()
    # look for links and dates
    links = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>([^<]{5,200})</a>', txt)
    return [(h, html.unescape(t).strip()) for h, t in links]

if __name__ == '__main__':
    rss = parse_rss('.tmp/0821b/m_*.html' if False else '.tmp/0821b/iaasia_rss.html')
