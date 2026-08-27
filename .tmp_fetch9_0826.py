#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, json, html as htmllib, subprocess, urllib.parse

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126"

def curl(url, timeout=35):
    return subprocess.run(["curl", "-sL", "--compressed", "--max-time", str(timeout), "-A", UA, url],
                          capture_output=True, text=True).stdout

def curl_head(url, timeout=30):
    r = subprocess.run(["curl", "-sIL", "--max-time", str(timeout), "-A", UA, url],
                       capture_output=True, text=True)
    return r.stdout

def clean(txt):
    txt = re.sub(r'<script.*?</script>', ' ', txt, flags=re.S)
    txt = re.sub(r'<style.*?</style>', ' ', txt, flags=re.S)
    txt = re.sub(r'<[^>]+>', ' ', txt)
    txt = htmllib.unescape(txt)
    return re.sub(r'\s+', ' ', txt).strip()

gnews_links = {
    'china-taiping': 'https://news.google.com/rss/articles/CBMi3gFBVV95cUxNdTNjd295Yk5HNWFSQ2dpSDJ5N1A3TmdPVFN1RS1ON2hjVVQ2VFY1Zy1pMU1jVWpSdkF0OHlYc3Z0WERFWmd1bk9wV0E0M0FaV3lCb24ydWN',
    'air-wealth': 'https://news.google.com/rss/articles/CBMi1wFBVV95cUxQMnRIYzZ3UFJnUzlvTmVVSzRQcWxGNkdqTXg3akxJY0FnZVFnLXgzVUFzQTVqUVg5VDVxQmstVmQtTHVKRkJvNkVGT3VhcjUzN0tCaHRzRnM',
    'taikang-ceo': 'https://news.google.com/rss/articles/CBMiuwFBVV95cUxQNjF1cGRiUTIyZzllbDRIOVFLa1JwdG5RWFlfZTctQ1JaT2JpQUZkNmMxOVBaMVBubi02UDZYRW1PYm85NFM0dkd4N25IVW9COFFEZUZmLVN',
    'hubbis-wealth': 'https://news.google.com/rss/articles/CBMi4wFBVV95cUxQTlF0cUtrTFhMY2dnUXJEU05VMU56Z25kd2RDN2pERHM0SE9uay1zbENtbVJXU3NnNHB3ejh2X09KOWJId1JpbmdmZF9uMU9CNXRWR0RNZU9',
}

print('===== resolve gnews redirects =====')
for tag, u in gnews_links.items():
    out = curl_head(u)
    last = [l for l in out.splitlines() if l.lower().startswith('location:')]
    print(f'--- {tag}: {last[-1].strip() if last else "no redirect (got page directly)"}')
    if not last:
        # try fetching the page and looking for og:url
        html = curl(u)
        m = re.search(r'<meta[^>]+property="og:url"[^>]+content="([^"]+)"', html)
        m2 = re.search(r'<meta[^>]+content="([^"]+)"[^>]+property="og:url"', html)
        print('   og:url:', (m.group(1) if m else (m2.group(1) if m2 else '?')))

print()
print('===== more Google News queries =====')
queries = [
    ('gnews-site-scmp', 'site:scmp.com insurance when:1d', 'en'),
    ('gnews-ia2', '保监局 when:2d', 'zh'),
    ('gnews-ia-en', '"Insurance Authority" Hong Kong when:2d', 'en'),
    ('gnews-famoffice2', '家族辦公室 香港 when:2d', 'zh'),
    ('gnews-cntaiping', '中国太平 保险 when:1d', 'zh'),
    ('gnews-hk-wealth', '香港 保險 財富 when:1d', 'zh'),
]
for tag, q, lang in queries:
    url = 'https://news.google.com/rss/search?q=' + urllib.parse.quote(q) + '&hl=' + lang + '&gl=HK&ceid=HK:' + lang
    print(f'=== {tag} ({q}) ===')
    try:
        xml = curl(url)
        items = re.findall(r'<item>(.*?)</item>', xml, re.S)
        print(f'  [{len(items)} items]')
        for it in items[:6]:
            t = re.search(r'<title>(.*?)</title>', it, re.S)
            l = re.search(r'<link>(.*?)</link>', it, re.S)
            p = re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
            src = re.search(r'<source[^>]*>(.*?)</source>', it, re.S)
            title = htmllib.unescape(t.group(1)).strip() if t else '?'
            print(f'  [{p.group(1).strip() if p else "?"}] ({src.group(1) if src else "?"}) {title[:90]}')
    except Exception as e:
        print('ERR', e)

print()
print('===== IBM body retry (raw html inspect) =====')
u = 'https://www.insurancebusinessmag.com/asia/news/breaking-news/steadfast-lifts-profit-as-us-consortium-moves-to-take-it-private-587463.aspx'
html = curl(u)
print('len:', len(html))
# find all div classes
classes = set(re.findall(r'<div class="([^"]+)"', html))
print('div classes:', sorted(classes)[:40])
# find meta description
m = re.search(r'<meta[^>]+name="description"[^>]+content="([^"]+)"', html)
print('meta description:', m.group(1)[:300] if m else '?')
m = re.search(r'<meta[^>]+property="og:description"[^>]+content="([^"]+)"', html)
print('og:description:', m.group(1)[:300] if m else '?')
# paragraphs inside article
m = re.search(r'<article[^>]*>(.*?)</article>', html, re.S)
if m:
    txt = clean(m.group(1))
    print('article text:', txt[:800])
