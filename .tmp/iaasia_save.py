#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Save InsuranceAsia HTML, then extract article links + dates."""
import re, subprocess, html

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
def fetch(url, t=30):
    return subprocess.run(["curl", "-sL", "--max-time", str(t), "-A", UA, url],
                          capture_output=True, text=True, timeout=t+10).stdout

raw = fetch("https://insuranceasia.com/insurance")
open(".tmp/iaasia-insurance.html", "w").write(raw)
print("saved", len(raw))

# all anchor hrefs
hrefs = re.findall(r'<a[^>]+href="([^"]+)"', raw)
print("anchors:", len(hrefs))
art = [h for h in hrefs if re.search(r"/(?:insurance|life|health|general|reinsurance)/[a-z0-9-]{12,}", h)]
uniq = list(dict.fromkeys(art))
print("article-ish unique:", len(uniq))
for u in uniq[:20]:
    print("  ", u[:140])

# look for datePublished / datetime attributes
dts = re.findall(r'(?:datetime|datePublished|content)="(20\d\d-\d\d-\d\d[^"]*)"', raw)
print("date attrs:", dts[:15])
