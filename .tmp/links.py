import json

c = json.load(open('.tmp/cands.json'))
e = json.load(open('.tmp/extra-cands.json'))

want = ["AIA profit surges", "This week in insurance", "Offshore reinsurance expands",
        "people moves", "Taikoo"]
print("== cands.json ==")
for k, v in c.items():
    for x in v:
        t = x.get("full_title") or x["title"]
        if any(w.lower() in t.lower() for w in want):
            print(k, "|", t[:70], "|", x["link"])
print("== extra-cands.json ==")
for q, v in e.items():
    for x in v:
        t = x["title"]
        if any(w.lower() in t.lower() for w in want + ["Ping An eyes", "Mainland insurers gain", "內地客來港"]):
            print("|", t[:75], "|", x["link"])
