import json
P = "/Users/leonliang/maoquanqingbao/data/last-check.json"
NOW = "2026-11-01T01:45:00+08:00"
d = json.load(open(P, encoding="utf-8"))
d["lastCheck"] = NOW
for k, v in d.get("sources", {}).items():
    if isinstance(v, dict):
        v["last"] = NOW
json.dump(d, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("lastCheck ->", d["lastCheck"], "| sources:", len(d["sources"]))
