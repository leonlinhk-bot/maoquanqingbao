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

def parse_bing(h, label):
    print(f'== BING {label}')
    blocks = re.findall(r'<li class="b_algo".*?</li>', h, re.S)
    print(f'  [blocks {len(blocks)}]')
    for b in blocks[:8]:
        # h2 link first
        m = re.search(r'<h2[^>]*>\s*<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', b, re.S)
        if not m:
            m = re.search(r'<a[^>]*href="(https?://[^"]+)"[^>]*>(.*?)</a>', b, re.S)
        if m:
            print('  -', clean(m.group(2))[:105], '|', m.group(1)[:100])
        else:
            txt = clean(b)[:120]
            print('  - (no link)', txt)

queries = [
    ('IA', 'site:ia.org.hk press release 27 August 2026'),
    ('NFRA', 'site:nfra.gov.cn 2026年8月27日 保险'),
    ('SCMP', 'site:scmp.com insurance 27 August 2026'),
    ('PRU', 'site:prudential.com.hk 2026 news'),
    ('HKMA-INS', 'site:hkma.gov.hk insurance 27 August 2026'),
]
for name, q in queries:
    url = 'https://www.bing.com/search?q=' + urllib.parse.quote(q) + '&count=10'
    try:
        parse_bing(fetch(url), name)
    except Exception as e:
        print(f'== BING {name} ERR {e}')
    time.sleep(1)

# FSTB press index
print('== FSTB press index')
try:
    h = fetch('https://www.fstb.gov.hk/en/news/press/index.php')
    print(f'  [len {len(h)}]')
    cnt = 0
    for m in re.finditer(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', h, re.S):
        t = clean(m.group(2))
        if t and (re.search(r'2026', t) or re.search(r'\d{1,2}/\d{1,2}/2026', m.group(1))):
            print('  -', t[:105], '|', m.group(1)[:100])
            cnt += 1
            if cnt >= 12:
                break
    print(f'  [total {cnt}]')
except Exception as e:
    print('  ERR', e)
