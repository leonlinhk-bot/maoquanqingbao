#!/usr/bin/env python3
import re, html

def body_text(path):
    raw = open(path, encoding='utf-8', errors='ignore').read()
    body = re.sub(r'<script.*?</script>', ' ', raw, flags=re.S)
    body = re.sub(r'<style.*?</style>', ' ', body, flags=re.S)
    body = re.sub(r'<[^>]+>', ' ', body)
    body = html.unescape(re.sub(r'\s+', ' ', body))
    return body

for f, label in [('.tmp/0821b/hkma_0821_3.html', 'HKMA 0821-3 PBOC RENMINBI BILLS'),
                 ('.tmp/0821b/hkma_0820_4.html', 'HKMA 0820-4 SCAM ALERT BANKS')]:
    b = body_text(f)
    m = re.search(r'<title>(.*?)</title>', open(f, encoding='utf-8', errors='ignore').read(), re.S)
    print('=' * 90)
    print(label)
    if m:
        print('TITLE:', html.unescape(m.group(1)).strip()[:120])
    # find the main content
    i = b.find('Hong Kong Monetary Authority')
    if i < 0:
        i = b.find('Press release')
    seg = b[i:i+1800] if i >= 0 else b[:1500]
    print(seg)
    print()
