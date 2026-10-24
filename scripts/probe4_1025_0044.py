#!/usr/bin/env python3
import os, re, urllib.request, urllib.parse, html, email.utils
from datetime import datetime, timezone, timedelta
HKT = timezone(timedelta(hours=8))
OUT = '/Users/leonliang/maoquanqingbao/data/_raw_1025_0044'
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36'
CUT = datetime(2026, 10, 24, 1, 8, tzinfo=HKT)

F = [
    ('air', 'https://www.asiainsurancereview.com/RSS'),
    ('air2', 'https://www.asiainsurancereview.com/rss/news'),
    ('captive', 'https://www.captivereview.com/feed/'),
    ('ibm_life', 'https://www.insurancebusinessmag.com/asia/news/life-insurance/rss/'),
    ('etnet', 'https://www.etnet.com.hk/www/tc/rss/news.php'),
    ('hket', 'https://www.hket.com/rss/finance'),
    ('mpf', 'https://www.mpfa.org.hk/rss/press.xml'),
    ('reinasia', 'https://www.reinasia.com/feed/'),
    ('swissre', 'https://www.swissre.com/rss/media.xml'),
]

def get(u):
    req = urllib.request.Request(u, headers={'User-Agent': UA, 'Accept': '*/*'})
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.read()

def pd(s):
    try:
        d = email.utils.parsedate_to_datetime(s)
        if d.tzinfo is None: d = d.replace(tzinfo=timezone.utc)
        return d.astimezone(HKT)
    except Exception:
        return None

for k, u in F:
    try:
        raw = get(u)
    except Exception as e:
        print(f'FAIL {k:9s} {type(e).__name__}: {str(e)[:60]}'); continue
    txt = raw.decode('utf-8', 'ignore')
    its = re.findall(r'<(item|entry)>(.*?)</\1>', txt, re.S)
    n = 0
    print(f'OK   {k:9s} {len(its)} items')
    for tag, b in its:
        d = re.search(r'<(pubDate|published|updated|dc:date)[^>]*>(.*?)</\1>', b, re.S)
        t = re.search(r'<title[^>]*>(.*?)</title>', b, re.S)
        lk = re.search(r'<link[^>]*href="([^"]+)"', b) or re.search(r'<link>(.*?)</link>', b, re.S)
        if not (d and t): continue
        dd = pd(re.sub(r'<[^>]+>', '', d.group(2)))
        if dd and dd >= CUT:
            n += 1
            title = html.unescape(re.sub(r'<[^>]+>', '', t.group(1)))
            print(f"   {dd.strftime('%m-%d %H:%M')} | {title[:88]}")
            print(f"      {(lk.group(1) if lk else '')[:110]}")
    if n == 0: print('   (nothing since 10-24 01:08)')
