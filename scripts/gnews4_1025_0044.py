#!/usr/bin/env python3
import urllib.request, urllib.parse, html, re, email.utils
from datetime import datetime, timezone, timedelta
HKT = timezone(timedelta(hours=8))
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36'

Q = [('保險', 'zh-HK', 'HK', 'HK:zh-Hant'),
     ('保监局', 'zh-CN', 'CN', 'CN:zh-Hans'),
     ('保险 监管', 'zh-CN', 'CN', 'CN:zh-Hans'),
     ('insurance', 'en-US', 'US', 'US:en')]

for q, hl, gl, ceid in Q:
    u = ('https://news.google.com/rss/search?q=' + urllib.parse.quote(q + ' when:2d') +
         f'&hl={hl}&gl={gl}&ceid={ceid}')
    try:
        req = urllib.request.Request(u, headers={'User-Agent': UA})
        txt = urllib.request.urlopen(req, timeout=25).read().decode('utf-8', 'ignore')
    except Exception as e:
        print('FAIL', q, type(e).__name__); continue
    its = re.findall(r'<item>(.*?)</item>', txt, re.S)
    print(f'\n== "{q} when:2d" ({len(its)})')
    for b in its[:15]:
        d = re.search(r'<pubDate>(.*?)</pubDate>', b, re.S)
        t = re.search(r'<title>(.*?)</title>', b, re.S)
        s = re.search(r'<source[^>]*>(.*?)</source>', b, re.S)
        try:
            ds = email.utils.parsedate_to_datetime(d.group(1)).astimezone(HKT).strftime('%m-%d %H:%M')
        except Exception:
            ds = '?'
        print(f"   {ds} [{(s.group(1) if s else '')[:15]}] {html.unescape(t.group(1))[:85]}")
