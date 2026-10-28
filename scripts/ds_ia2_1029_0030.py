#!/usr/bin/env python3
"""IA press releases 多路径探测（DeepSeek fetch 绕过 CF）。"""
import json, os, urllib.request

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
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read().decode())


urls = [
    "https://www.ia.org.hk/en/infocenter/press_releases/",
    "https://www.ia.org.hk/tc/infocenter/press_releases.html",
    "https://www.ia.org.hk/en/infocenter/index.html",
]
for u in urls:
    print("=" * 60)
    print(u)
    try:
        res = call("/v1/tools/fetch", {"url": u})
        c = res.get("content") or ""
        print("len", len(c))
        print(c[:1800])
    except Exception as e:
        print("ERR", type(e).__name__, e)
