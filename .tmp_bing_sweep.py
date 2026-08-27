#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, html, urllib.request, ssl, urllib.parse, time

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def clean(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()

def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept-Language': 'en-US,en;q=0.9'})
    with urllib.request.urlopen(req, timeout=30, context=ctx) as r:
        return r.read().decode('utf-8', 'replace')

# 1) FSTB press releases list
print('== FSTB press releases')
try:
    h = fetch('https://www.fstb.gov.hk/en/others/press-releases.html')
    for m in re.finditer(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', h, re.S):
        t = clean(m.group(2))
        if t and ('2026' in t or re.search(r'\d{1,2}\s+\w+\s+2026', t)):
            print('  -', t[:110], '|', m.group(1)[:110])
except Exception as e:
    print('  ERR', e)

# 2) Bing searches
queries = [
    ('IA', 'site:ia.org.hk 保监局 OR press release August 2026'),
    ('NFRA', 'site:nfra.gov.cn 金融监管总局 2026年8月27日'),
    ('SCMP', 'site:scmp.com insurance August 27 2026'),
    ('PRU', 'site:prudential.com.hk newsroom August 2026'),
    ('AXA', 'site:axa.com.hk news August 2026'),
]
for name, q in queries:
    print(f'== BING {name}: {q}')
    url = 'https://www.bing.com/search?q=' + urllib.parse.quote(q) + '&count=10'
    try:
        h = fetch(url)
        blocks = re.findall(r'<li class="b_algo".*?</li>', h, re.S)
        print(f'  [blocks {len(blocks)}]')
        for b in blocks[:8]:
            tm = re.search(r'<h2><a[^>]*href="([^"]+)"[^>]*>(.*?)</a></h2>', b, re.S)
            if tm:
                print('  -', clean(tm.group(2))[:100], '|', tm.group(1)[:100])
        if not blocks:
            # fallback: any h2 links
            for tm in re.finditer(r'<h2><a[^>]*href="([^"]+)"[^>]*>(.*?)</a></h2>', h, re.S)[:8]:
                print('  -', clean(tm.group(2))[:100], '|', tm.group(1)[:100])
    except Exception as e:
        print('  ERR', e)
    time.sleep(1)
