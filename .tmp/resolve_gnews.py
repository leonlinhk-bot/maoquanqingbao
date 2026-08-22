#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Resolve Google News redirect links to real article URLs."""
import json, subprocess, re, sys

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"

def resolve(gnurl, t=30):
    try:
        r = subprocess.run(["curl", "-sL", "--max-time", str(t), "-A", UA,
                            "-o", "/dev/null", "-w", "%{url_effective}", gnurl],
                           capture_output=True, text=True, timeout=45)
        return r.stdout
    except Exception as e:
        return f"ERR {e}"

sweep = json.load(open("data/_raw/t0822b/gnews-sweep.json"))
targets = sys.argv[1:] if len(sys.argv) > 1 else [
    "nfra", "fstb", "hkma-news", "mcv", "insurtech", "aia-news", "china-tax", "premfin", "ib-news"]
seen = set()
for tag in targets:
    if tag not in sweep: continue
    print(f"\n=== {tag} ===")
    for r in sweep[tag]["fresh"][:8]:
        link = r["link"]
        if link in seen: continue
        seen.add(link)
        real = resolve(link)
        print(f"  [{r['dt'][:16]}] {r['src'][:18]:18s} {r['title'][:70]}")
        print(f"    REAL: {real[:150]}")
