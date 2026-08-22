#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deep-inspect InsuranceAsia homepage + sitemap pages for article links w/ dates."""
import re, subprocess, html

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
def fetch(url, t=30):
    try:
        return subprocess.run(["curl", "-sL", "--max-time", str(t), "-A", UA, url],
                              capture_output=True, text=True, timeout=t+10).stdout
    except Exception as e:
        return f"ERR {e}"

# 1. look for any hrefs that look like article slugs
raw = fetch("https://insuranceasia.com/insurance")
hrefs = re.findall(r'href="([^"]+)"', raw)
print("total hrefs:", len(hrefs))
arts = [h for h in hrefs if re.search(r"/(insurance|life|health|general|reinsurance)/[a-z0-9-]{15,}", h)]
seen = set()
for h in arts:
    if h not in seen:
        seen.add(h)
        print("  ART:", h[:130])
print("unique article-ish:", len(seen))

# 2. check for JSON-LD or meta og:title with dates
m = re.findall(r'"(datePublished|published_date|dateModified)":"([^"]+)"', raw)
print("datePublished in JSON:", m[:10])

# 3. sitemap page 1
raw2 = fetch("https://insuranceasia.com/11/sitemap.xml?page=1")
urls = re.findall(r"<loc>([^<]+)</loc>", raw2)
print("\nsitemap p1 urls:", len(urls))
for u in urls[:25]:
    print("  ", u[:130])
