#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Try InsuranceAsia Drupal JSON API + IBmag article dates."""
import re, subprocess, html, json

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
def fetch(url, t=30):
    return subprocess.run(["curl", "-sL", "--max-time", str(t), "-A", UA, url],
                          capture_output=True, text=True, timeout=t+10).stdout

# 1. InsuranceAsia JSON API attempts
for url in [
    "https://insuranceasia.com/jsonapi/node/article?sort=-created&page[limit]=15",
    "https://insuranceasia.com/rest/views/articles?page=0",
]:
    raw = fetch(url)
    print(f"== {url}: {len(raw)} bytes")
    print(raw[:300].replace("\n", " "))
    try:
        j = json.loads(raw)
        print("  parsed OK; keys:", list(j.keys())[:5])
        if "data" in j:
            for d in j["data"][:10]:
                attrs = d.get("attributes", {})
                print("   -", attrs.get("title", "?")[:80], "|", attrs.get("created", ""))
    except Exception:
        pass
    print()

# 2. IBmag breaking news page: find article cards with dates
raw = fetch("https://www.insurancebusinessmag.com/asia/news/breaking-news/")
open(".tmp/ibmag-bn.html", "w").write(raw)
print("ibmag saved", len(raw))
# find date-ish patterns
dts = re.findall(r"(20\d\d-\d\d-\d\d)", raw)
from collections import Counter
print("dates:", Counter(dts).most_common(15))
