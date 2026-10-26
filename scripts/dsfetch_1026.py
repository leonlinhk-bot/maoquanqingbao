import json, os, re, sys, urllib.request

key = None
for line in open(os.path.expanduser("~/.hermes/.env"), encoding="utf-8", errors="replace"):
    if line.startswith("DEEPSEEK_API_KEY="):
        key = line.split("=", 1)[1].strip().strip('"').strip("'")
        break
assert key, "no key"

def call(path, payload):
    req = urllib.request.Request(
        "https://api.deepseek.com" + path,
        data=json.dumps(payload).encode(),
        headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.loads(r.read().decode())

urls = [
    "https://www.ia.org.hk/en/infocenter/press_releases.html",
    "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html",
]
for u in urls:
    print("=" * 30)
    print(u)
    try:
        res = call("/v1/tools/fetch", {"url": u})
        c = res.get("content") if isinstance(res, dict) else None
        if c is None:
            print(json.dumps(res, ensure_ascii=False)[:800])
        else:
            print("len", len(c))
            print(c[:3000])
    except Exception as e:
        print("ERR", type(e).__name__, str(e)[:300])
