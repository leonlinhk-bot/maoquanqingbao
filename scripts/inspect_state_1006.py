import json, os, glob

base = "/Users/leonliang/maoquanqingbao"
d = json.load(open(os.path.join(base, "data/live-items.json")))
print("META:", json.dumps(d.get("meta", {}), ensure_ascii=False))
print("N items:", len(d["items"]))
print("--- newest 15 ---")
for it in d["items"][:15]:
    print(it.get("publishedAt"), "|", it.get("sourceKey"), "|", it.get("sourceTier"), "|", it.get("title", {}).get("sc", "")[:44])
print("--- distinct sourceKeys in items ---")
from collections import Counter
c = Counter(it.get("sourceKey") for it in d["items"])
print(dict(c))
print("--- scripts present ---")
print(sorted(os.listdir(os.path.join(base, "scripts"))))
print("--- posters dir ---")
p = os.path.join(base, "posters")
print(sorted(os.listdir(p))[-8:] if os.path.isdir(p) else "NO POSTERS DIR")
