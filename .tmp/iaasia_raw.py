#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Raw check: what does insuranceasia return now."""
import subprocess

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
def fetch(url, t=30):
    return subprocess.run(["curl", "-sL", "--max-time", str(t), "-A", UA, url],
                          capture_output=True, text=True, timeout=t+10).stdout

for url in ["https://insuranceasia.com/", "https://insuranceasia.com/insurance"]:
    raw = fetch(url)
    print(f"== {url}: {len(raw)} bytes")
    print(raw[:400].replace("\n", " "))
    print()
