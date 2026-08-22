import subprocess, re, html

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"

def fetch(url):
    return subprocess.run(["curl", "-sL", "--max-time", "30", "-A", UA, url],
                          capture_output=True, text=True).stdout

def clean(raw):
    raw = re.sub(r"<script.*?</script>|<style.*?</style>", " ", raw, flags=re.S)
    raw = re.sub(r"<[^>]+>", " ", raw)
    return re.sub(r"\s+", " ", html.unescape(raw)).strip()

# IA people moves URL guess
u = "https://insuranceasia.com/insurance/news/aon-zurich-marsh-aig-allianz-trade-18-apac-insurance-people-moves-of-the-week"
raw = fetch(u)
print("IA people len:", len(raw))
t = re.search(r'<meta property="og:title" content="([^"]+)"', raw)
print("OG:", html.unescape(t.group(1)) if t else "?")
txt = clean(raw)
i = txt.find("people moves")
print(txt[max(0, i-100):i+1200])

# wenweipo article: find via bing apiclick
q_url = "https://www.bing.com/news/search?q=%E5%8F%8B%E9%82%A6%E5%8D%8A%E5%B9%B4%E7%B4%94%E5%88%A9%E5%A4%A7%E5%A2%9E+%E5%85%A7%E5%9C%B0%E5%AE%A2%E6%8A%95%E4%BF%9D%E9%9C%80%E6%B1%82&format=rss"
raw2 = fetch(q_url)
print("\n=== wenweipo bing hits ===")
for it in re.findall(r"<item>(.*?)</item>", raw2, re.S):
    t = re.search(r"<title>(.*?)</title>", it, re.S)
    l = re.search(r"<link>(.*?)</link>", it, re.S)
    print("-", html.unescape(t.group(1))[:80] if t else "")
    link = html.unescape(l.group(1)) if l else ""
    if "apiclick" in link:
        real = subprocess.run(["curl", "-sL", "--max-time", "25", "-A", UA, "-o", "/dev/null", "-w", "%{url_effective}", link],
                              capture_output=True, text=True).stdout
        print("  REAL:", real[:140])
