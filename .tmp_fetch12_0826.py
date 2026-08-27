#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, json, html as htmllib, subprocess, urllib.parse

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126"

def curl(url, timeout=35, post=None, headers=None):
    cmd = ["curl", "-sL", "--compressed", "--max-time", str(timeout), "-A", UA]
    if headers:
        for h in headers:
            cmd += ["-H", h]
    if post:
        cmd += ["-X", "POST", "-d", post]
    cmd.append(url)
    return subprocess.run(cmd, capture_output=True, text=True).stdout

def clean(txt):
    txt = re.sub(r'<script.*?</script>', ' ', txt, flags=re.S)
    txt = re.sub(r'<style.*?</style>', ' ', txt, flags=re.S)
    txt = re.sub(r'<[^>]+>', ' ', txt)
    txt = htmllib.unescape(txt)
    return re.sub(r'\s+', ' ', txt).strip()

print('===== 1. HKEX title search: China Taiping (966) =====')
post = ('lang=CH&category=0&market=SEHK&searchType=1&documentType=-1&fromDate=20260824'
        '&toDate=20260826&title=&stockId=966')
try:
    txt = curl('https://www1.hkexnews.hk/search/titleSearchServlet.do', post=post,
               headers=['Content-Type: application/x-www-form-urlencoded',
                        'Referer: https://www1.hkexnews.hk/search/titlesearch.xhtml?lang=CH'])
    print('len:', len(txt))
    print(txt[:2000])
except Exception as e:
    print('ERR', e)

print()
print('===== 2. Sina search: 巴克萊 離岸資產 =====')
try:
    html = curl('https://search.sina.com.cn/?q=' + urllib.parse.quote('巴克萊 離岸資產監管 香港'))
    print('len:', len(html))
    for m in re.finditer(r'<h2><a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', html, re.S)[:0] or re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', html, re.S):
        href, t = m.group(1), clean(m.group(2))
        if len(t) > 8 and ('finance' in href or 'sina' in href or 'stock' in href):
            print('  ', t[:80], '->', href[:130])
except Exception as e:
    print('ERR', e)

print()
print('===== 3. SCMP search API =====')
for u in ['https://gateway.scmp.com/search?q=' + urllib.parse.quote('Beijing targets cross-border corruption'),
          'https://search.scmp.com/s/search?q=' + urllib.parse.quote('cross-border corruption Hong Kong markets brace')]:
    try:
        txt = curl(u)
        print(f'--- {u[:90]} len={len(txt)}')
        print(txt[:600])
    except Exception as e:
        print('ERR', e)

print()
print('===== 4. on.cc / stheadline site search via Bing RSS =====')
for q in ['site:on.cc 巴克萊 離岸資產', 'site:stheadline.com 巴克萊 離岸', 'site:hket.com 吳光正 家族辦公室']:
    xml = curl('https://www.bing.com/search?q=' + urllib.parse.quote(q) + '&format=rss&count=10')
    print(f'--- {q}')
    for m in re.findall(r'<item>(.*?)</item>', xml, re.S)[:5]:
        t = re.search(r'<title>(.*?)</title>', m, re.S)
        l = re.search(r'<link>(.*?)</link>', m, re.S)
        title = htmllib.unescape(t.group(1)).strip() if t else '?'
        link = htmllib.unescape(l.group(1)).strip() if l else '?'
        if 'on.cc' in link or 'stheadline' in link or 'hket' in link or 'wikipedia' in link:
            print('  ', title[:85])
            print('     ', link[:150])
