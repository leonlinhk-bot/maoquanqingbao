#!/usr/bin/env python3
import urllib.request, urllib.parse, html, re, email.utils
from datetime import datetime, timezone, timedelta
HKT = timezone(timedelta(hours=8))
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36'

Q = ['保監局 通函', '香港 保險 經紀', '內地訪客 保險', '香港 危疾保險',
     '香港 強積金 積金局', '保险 新规 发布', '香港 保險 招聘 人事',
     'Hong Kong insurance broker', 'Hong Kong wealth management family office',
     'captive insurance Asia regulator', 'Taiwan insurance regulator',
     'Hong Kong MPF eMPF']

def gn(q):
    u = 'https://news.google.com/rss/search?q=' + urllib.parse.quote(q) + '&hl=zh-HK&gl=HK&ceid=HK:zh-Hant'
    req = urllib.request.Request(u, headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=25) as r:
        return r.read().decode('utf-8', 'ignore')

for q in Q:
    try:
        txt = gn(q)
    except Exception as e:
        print('FAIL', q, type(e).__name__); continue
    its = re.findall(r'<item>(.*?)</item>', txt, re.S)
    print(f'\n== {q} ({len(its)})')
    for b in its[:8]:
        d = re.search(r'<pubDate>(.*?)</pubDate>', b, re.S)
        t = re.search(r'<title>(.*?)</title>', b, re.S)
        s = re.search(r'<source[^>]*>(.*?)</source>', b, re.S)
        try:
            dd = email.utils.parsedate_to_datetime(d.group(1)).astimezone(HKT)
            ds = dd.strftime('%m-%d %H:%M')
        except Exception:
            ds = '?'
        mark = '  <<< ' if ds.startswith('10-2') and (ds.startswith('10-24') or ds.startswith('10-25')) else ''
        print(f"   {ds} [{(s.group(1) if s else '')[:16]}] {html.unescape(t.group(1))[:88]}{mark}")
