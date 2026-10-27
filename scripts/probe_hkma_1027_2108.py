#!/usr/bin/env python3
"""HKMA press release titles+dates, SCMP insurance-ish 27 Oct items."""
import re, urllib.request

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"}

def get(url):
    req = urllib.request.Request(url, headers=UA)
    return urllib.request.urlopen(req, timeout=30).read().decode('utf-8', 'ignore')

h = get("https://www.hkma.gov.hk/eng/news-and-media/press-releases/")
# find rows with date 27 Oct 2026
blocks = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', h, re.S)
print("=== HKMA links sample ===")
for u, t in blocks[:40]:
    txt = re.sub(r'<[^>]+>', '', t).strip()
    if txt and len(txt) > 15:
        print(txt[:110], '|', u[:100])

print("\n=== HKMA 27 Oct context ===")
for m in re.finditer(r'27 Oct 2026', h):
    print(repr(h[max(0, m.start()-400):m.start()+200].replace('\n',' '))[:600])
    print('---')
