import json, subprocess

c = json.load(open('.tmp/cands.json'))
e = json.load(open('.tmp/extra-cands.json'))

def resolve(url):
    return subprocess.run(["curl", "-sL", "--max-time", "25", "-A",
                           "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36",
                           "-o", "/dev/null", "-w", "%{url_effective}", url],
                          capture_output=True, text=True).stdout

print("== cands.json bing entries ==")
for k, v in c.items():
    if k.startswith("bing"):
        for x in v:
            print(k, "|", x["title"][:70], "|", x["link"][:90])

print("== extra-cands.json all ==")
seen = set()
for q, v in e.items():
    for x in v:
        key = x["title"][:50]
        if key in seen:
            continue
        seen.add(key)
        print("|", x["title"][:70], "|", x["link"][:80])
        if "apiclick" in x["link"]:
            real = resolve(x["link"])
            print("   ->", real[:130])
