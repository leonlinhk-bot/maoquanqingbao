#!/usr/bin/env python3
"""Dump IA press-release list (via DeepSeek fetch, CF bypass) — show newest entries."""
import json, os, re, urllib.request

key = None
for line in open(os.path.expanduser("~/.hermes/.env"), encoding="utf-8", errors="replace"):
    if line.startswith("DEEPSEEK_API_KEY="):
        key = line.split("=", 1)[1].strip().strip('"').strip("'")
        break
assert key

def call(path, payload):
    req = urllib.request.Request("https://api.deepseek.com" + path,
        data=json.dumps(payload).encode(),
        headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.loads(r.read().decode())

for u in ["https://www.ia.org.hk/en/infocenter/press_releases.html",
          "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html"]:
    print("=" * 40)
    print(u)
    try:
        res = call("/v1/tools/fetch", {"url": u})
        c = res.get("content") or ""
        print("len", len(c))
        # print tail where lists normally live
        print(c[-3500:])
    except Exception as e:
        print("ERR", type(e).__name__, e)
