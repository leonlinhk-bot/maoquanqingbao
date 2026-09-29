import json, os
NOW = "2026-09-29T09:30:00+08:00"
p = "data/last-check.json"
d = json.load(open(p, encoding="utf-8"))
d["lastCheck"] = NOW
for k, v in d["sources"].items():
    if isinstance(v, dict):
        v["last"] = NOW
json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("lastCheck ->", d["lastCheck"], "| sources:", len(d["sources"]))
print("all last==NOW:", all(v.get("last") == NOW for v in d["sources"].values()))
