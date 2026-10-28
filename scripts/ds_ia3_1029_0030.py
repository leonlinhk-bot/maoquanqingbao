#!/usr/bin/env python3
import json, os, urllib.request

key = None
for line in open(os.path.expanduser("~/.hermes/.env"), encoding="utf-8", errors="replace"):
    if line.startswith("DEEPSEEK_API_KEY="):
        key = line.split("=", 1)[1].strip().strip('"').strip("'")
        break


def call(path, payload):
    req = urllib.request.Request("https://api.deepseek.com" + path,
        data=json.dumps(payload).encode(),
        headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read().decode())


res = call("/v1/tools/fetch", {"url": "https://www.ia.org.hk/en/infocenter/press_releases/"})
c = res.get("content") or ""
print("LEN", len(c))
print(c[3000:])
