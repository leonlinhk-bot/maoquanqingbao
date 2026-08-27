#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, json, html as htmllib, subprocess, urllib.request

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126"

def curl(url, timeout=35):
    return subprocess.run(["curl", "-sL", "--compressed", "--max-time", str(timeout), "-A", UA, url],
                          capture_output=True, text=True).stdout

def clean(txt):
    txt = re.sub(r'<script.*?</script>', ' ', txt, flags=re.S)
    txt = re.sub(r'<style.*?</style>', ' ', txt, flags=re.S)
    txt = re.sub(r'<[^>]+>', ' ', txt)
    txt = htmllib.unescape(txt)
    return re.sub(r'\s+', ' ', txt).strip()

print('===== 1. Wayback CDX: ia.org.hk press releases recent =====')
u = ('http://web.archive.org/cdx/search/cdx?url=ia.org.hk/en/infocenter/press_releases*'
     '&from=20260820&to=20260826&output=json&limit=60&collapse=urlkey')
try:
    txt = curl(u)
    rows = json.loads(txt)
    print('rows:', len(rows) - 1)
    for r in rows[1:40]:
        print('  ', r[1], r[2][:110])
except Exception as e:
    print('ERR', e)

print()
print('===== 2. Wayback availability: IA press releases page =====')
u = 'http://archive.org/wayback/available?url=ia.org.hk/en/infocenter/press_releases.html&timestamp=20260826120000'
try:
    txt = curl(u)
    print(txt[:500])
except Exception as e:
    print('ERR', e)

print()
print('===== 3. NFRA ItemList.json =====')
for u in ['https://www.nfra.gov.cn/cn/view/pages/ItemList.json?itemPId=921&itemId=922',
          'https://www.nfra.gov.cn/cn/view/pages/ItemList.json?itemPId=923&itemId=924']:
    txt = curl(u)
    print(f'--- {u}\n  len={len(txt)} first500={txt[:500]}')

print()
print('===== 4. Hubbis / Asia Insurance Review wealth insurance =====')
# find real hubbis url via bing rss
xml = curl('https://www.bing.com/search?q=' + urllib.parse.quote('Hubbis international wealth insurance adoption Asia') + '&format=rss&count=10')
for m in re.finditer(r'<item>(.*?)</item>', xml, re.S):
    t = re.search(r'<title>(.*?)</title>', m.group(1), re.S)
    l = re.search(r'<link>(.*?)</link>', m.group(1), re.S)
    print('  ', (htmllib.unescape(t.group(1)).strip()[:80] if t else '?'))
    print('    ', (htmllib.unescape(l.group(1)).strip()[:150] if l else '?'))

print()
print('===== 5. IBM article bodies =====')
for tag, u in [
    ('sg-west-island', 'https://www.insurancebusinessmag.com/asia/news/construction/singapores-new-western-island-will-need-insurance-tools-that-do-not-yet-exist-587445.aspx'),
    ('sg-cfo', 'https://www.insurancebusinessmag.com/asia/news/professional-liability/singapores-cfo-confidence-crash-conceals-a-broker-opening-587444.aspx'),
    ('steadfast', 'https://www.insurancebusinessmag.com/asia/news/breaking-news/steadfast-lifts-profit-as-us-consortium-moves-to-take-it-private-587463.aspx'),
]:
    try:
        html = curl(u)
        body = ''
        m = re.search(r'<article[^>]*>(.*?)</article>', html, re.S)
        if m:
            body = clean(m.group(1))
        if not body:
            m = re.search(r'<div class="article-body[^"]*"[^>]*>(.*?)</div>', html, re.S)
            if m:
                body = clean(m.group(1))
        print(f'--- {tag} | body: {body[:600]}')
    except Exception as e:
        print(f'--- {tag} ERR {e}')
