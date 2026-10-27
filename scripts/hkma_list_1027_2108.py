#!/usr/bin/env python3
"""HKMA press releases dated 27 Oct 2026 + last 3 days list."""
import re, urllib.request

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0"}
req = urllib.request.Request("https://www.hkma.gov.hk/eng/news-and-media/press-releases/", headers=UA)
h = urllib.request.urlopen(req, timeout=30).read().decode('utf-8', 'ignore')

seg = h.split('id="press-release-result"')[1][:8000]
rows = re.findall(r'<li>(\d{1,2} \w{3} 2026)</li>\s*<li><a href="([^"]+)"[^>]*(?:title="([^"]*)")?[^>]*>(.*?)</a>', seg, re.S)
for d, u, t, txt in rows:
    t2 = t or re.sub(r'<[^>]+>', '', txt).strip()
    print(f"{d} | {t2[:100]} | https://www.hkma.gov.hk{u}")
