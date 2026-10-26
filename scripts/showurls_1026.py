import json, subprocess, re, html

d = json.load(open("/tmp/feeds_1026.json"))
for k in ("insuranceasia", "ibm_asia", "govhk", "ian_wp", "reinsurancenews", "artemis"):
    v = d.get(k, [])
    print("=" * 25, k, len(v))
    for row in v[:8]:
        print(json.dumps(row, ensure_ascii=False)[:260])
