#!/usr/bin/env python3
import urllib.request, urllib.parse, html, re, email.utils, json
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36'

Q = ['分紅保單 兩年一檢', '電動車 汽車保險 保障 香港01 周小斐',
     'NTT DATA Insurtech Global Outlook 2026', '險資 算力 產業']

for q in Q:
    u = ('https://news.google.com/rss/search?q=' + urllib.parse.quote(q) +
         '&hl=zh-HK&gl=HK&ceid=HK:zh-Hant')
    try:
        txt = urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': UA}),
                                     timeout=25).read().decode('utf-8', 'ignore')
    except Exception as e:
        print('FAIL', q, e); continue
    print(f'\n== {q}')
    for b in re.findall(r'<item>(.*?)</item>', txt, re.S)[:5]:
        t = re.search(r'<title>(.*?)</title>', b, re.S)
        l = re.search(r'<link>(.*?)</link>', b, re.S)
        d = re.search(r'<pubDate>(.*?)</pubDate>', b, re.S)
        print('  ', d.group(1)[:25] if d else '?', '|', html.unescape(t.group(1))[:80] if t else '')
        print('    ', l.group(1) if l else '')
