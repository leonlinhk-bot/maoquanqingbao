#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, json, html as htmllib, subprocess, urllib.parse

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/126.0.0.0 Safari/537.36")

def curl(url, timeout=35, headers=None):
    cmd = ["curl", "-sL", "--compressed", "--max-time", str(timeout), "-A", UA,
           "-H", "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "-H", "Accept-Language: en-US,en;q=0.9,zh-HK;q=0.8"]
    if headers:
        for h in headers:
            cmd += ["-H", h]
    cmd.append(url)
    return subprocess.run(cmd, capture_output=True, text=True).stdout

gnews = {
    'scmp-corruption': 'https://news.google.com/rss/articles/CBMi3gFBVV95cUxNdTNjd295Yk5HNWFSQ2dpSDJ5N1A3TmdPVFN1RS1ON2hjVVQ2VFY1Zy1pMU1jVWpSdkF0OHlYc3Z0WERFWmd1bk9wV0E0M0FaV3lCb24ydWN',
    'taikang-ceo': 'https://news.google.com/rss/articles/CBMiuwFBVV95cUxQNjF1cGRiUTIyZzllbDRIOVFLa1JwdG5RWFlfZTctQ1JaT2JpQUZkNmMxOVBaMVBubi02UDZYRW1PYm85NFM0dkd4N25IVW9COFFEZUZmLVN',
    'hubbis-wealth': 'https://news.google.com/rss/articles/CBMi4wFBVV95cUxQTlF0cUtrTFhMY2dnUXJEU05VMU56Z25kd2RDN2pERHM0SE9uay1zbENtbVJXU3NnNHB3ejh2X09KOWJId1JpbmdmZF9uMU9CNXRWR0RNZU9',
}

print('===== resolve gnews article pages =====')
for tag, u in gnews.items():
    html = curl(u)
    print(f'--- {tag} len={len(html)}')
    # look for real urls
    found = set()
    for pat in [r'https://www\.scmp\.com[^"\\\s]+', r'https://[a-z0-9.-]*air\.[a-z]+[^"\\\s]*',
                r'https://hubbis\.com[^"\\\s]*', r'https://[a-z0-9.-]*slipcase[^"\\\s]*',
                r'https://[a-z0-9.-]*reinasia[^"\\\s]*', r'https://[a-z0-9.-]*insurancenewsnet[^"\\\s]*']:
        for m in re.findall(pat, html):
            if m not in found:
                found.add(m)
                print('   ', m[:170])
    if not found:
        # look for any external http links
        for m in re.findall(r'https?://[a-z0-9.-]+\.[a-z]{2,6}/[^"\\\s<]{10,150}', html):
            if 'google' not in m and 'gstatic' not in m and 'ggpht' not in m:
                print('   ?', m[:170])
                if len(found) > 8:
                    break
                found.add(m)

print()
print('===== HKEX GET attempt =====')
u = ('https://www1.hkexnews.hk/search/titleSearchServlet.do?lang=CH&category=0&market=SEHK'
     '&searchType=1&documentType=-1&fromDate=20260824&toDate=20260826&title=&stockId=966')
txt = curl(u)
print('len:', len(txt))
print(txt[:1500])
