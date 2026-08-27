#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Map article titles -> canonical URLs from InsuranceAsia + IBM homepages."""
import re, html as H

def anchors(path):
    html = open(path, encoding='utf-8', errors='replace').read()
    out = []
    for href, txt in re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', html, re.S):
        txt = H.unescape(re.sub(r'<[^>]+>', ' ', txt))
        txt = re.sub(r'\s+', ' ', txt).strip()
        if txt and len(txt) >= 15:
            out.append((txt, href))
    return out

print('===== InsuranceAsia (iaa.html) =====')
for t, h in anchors('/Users/leonliang/.tmp/scan0826/iaa.html'):
    if '/insurance/' in h and h.startswith('https://insuranceasia.com'):
        print('|', t[:80], '|', h)
print()
print('===== IBM (ibm.html) =====')
for t, h in anchors('/Users/leonliang/.tmp/scan0826/ibm.html'):
    if h.startswith('/asia/news'):
        print('|', t[:80], '|', 'https://www.insurancebusinessmag.com' + h)
