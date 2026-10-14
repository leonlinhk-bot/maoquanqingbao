#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Check FSTB blog/news for in-window posts."""
import gzip, zlib, re, html, urllib.request

PROXY = 'http://127.0.0.1:17891'
UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/126.0 Safari/537.36')


def get(url, timeout=25):
    err = ''
    for proxy in (PROXY, None):
        h = {'http': proxy, 'https': proxy} if proxy else {}
        op = urllib.request.build_opener(urllib.request.ProxyHandler(h))
        op.addheaders = [('User-Agent', UA), ('Accept', '*/*')]
        try:
            r = op.open(url, timeout=timeout)
            raw = r.read()
            if r.headers.get('Content-Encoding') == 'gzip':
                raw = gzip.decompress(raw)
            return raw.decode('utf-8', 'replace')
        except Exception as e:
            err = f'__ERR__ {type(e).__name__}: {str(e)[:100]}'
    return err


def strip(s):
    s = re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>', '', s or '')
    s = re.sub(r'(?s)<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()


for u in ['https://www.fstb.gov.hk/en/blog/blog.htm',
          'https://www.fstb.gov.hk/tc/blog/blog.htm',
          'https://www.fstb.gov.hk/en/news/index.htm',
          'https://www.fstb.gov.hk/tc/news/']:
    t = get(u)
    print('===', u, len(t) if not t.startswith('__ERR__') else t)
    if not t.startswith('__ERR__'):
        txt = strip(t)
        print(txt[:700])
        print('--- dates found:', sorted(set(re.findall(r'\d{1,2}[./]\d{1,2}[./]20\d\d|20\d\d-\d\d-\d\d|\d{1,2} \w+ 20\d\d', txt)))[-8:])
