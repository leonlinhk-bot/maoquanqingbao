#!/usr/bin/env python3
"""IA 列表页经 DeepSeek fetch 绕过 Cloudflare，确认有无新稿/新通函。"""
import json, os, re, urllib.request

key = None
for line in open(os.path.expanduser("~/.hermes/.env"), encoding="utf-8", errors="replace"):
    if line.startswith("DEEPSEEK_API_KEY="):
        key = line.split("=", 1)[1].strip().strip('"').strip("'")
        break
assert key, 'no DEEPSEEK_API_KEY'


def call(path, payload):
    req = urllib.request.Request("https://api.deepseek.com" + path,
        data=json.dumps(payload).encode(),
        headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read().decode())


urls = [
    ("IA press", "https://www.ia.org.hk/en/infocenter/press_releases.html"),
    ("IA circular 2026", "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html"),
]
for label, u in urls:
    print("=" * 60)
    print(label, u)
    try:
        res = call("/v1/tools/fetch", {"url": u})
        c = res.get("content") or ""
        print("len", len(c))
        print(c[:2500])
    except Exception as e:
        print("ERR", type(e).__name__, e)
