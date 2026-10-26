import re, subprocess, json, os, urllib.request
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120 Safari/537.36"

def get(url, t=25):
    r = subprocess.run(["curl", "-m", str(t), "-sL", "-A", UA, url], capture_output=True, text=True, errors="replace")
    return r.stdout

sites = {
    "aia": "https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases/",
    "prudential": "https://www.prudential.com.hk/tc/about-us/newsroom/",
    "manulife": "https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html",
    "axa": "https://www.axa.com.hk/zh/news-room/",
    "sunlife": "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/",
    "hkfi": "https://www.hkfi.org.hk/en/media-centre/press-release",
}
for k, u in sites.items():
    h = get(u)
    hits = re.findall(r"(2026[-/年]\s?0?9[-/月]\s?\d{1,2}|2026[-/年]\s?10[-/月]\s?\d{1,2}|\d{1,2}\s+(?:Oct|Sep|October|September)[a-z]*\s+2026)", h)
    from collections import Counter
    print("==", k, "bytes", len(h), "datehits", Counter(hits).most_common(6))

# DeepSeek fetch for NFRA news list
key = None
for line in open(os.path.expanduser("~/.hermes/.env"), encoding="utf-8", errors="replace"):
    if line.startswith("DEEPSEEK_API_KEY="):
        key = line.split("=", 1)[1].strip().strip('"').strip("'")
        break
print("\nDEEPSEEK key:", bool(key))

def call(path, payload):
    req = urllib.request.Request("https://api.deepseek.com" + path, data=json.dumps(payload).encode(),
                                 headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.loads(r.read().decode())

for u in ["https://www.nfra.gov.cn/cn/view/pages/ItemList.html?itemPId=923&itemId=915",
          "https://www.hkfi.org.hk/en/media-centre/press-release"]:
    try:
        res = call("/v1/tools/fetch", {"url": u})
        c = res.get("content", "")
        print("\n=== FETCH", u, "len", len(c))
        print(c[:1800])
    except Exception as e:
        print("ERR", u, type(e).__name__, str(e)[:200])
