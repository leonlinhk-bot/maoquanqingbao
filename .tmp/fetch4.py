import subprocess, re, html, urllib.parse, datetime

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
TZ8 = datetime.timezone(datetime.timedelta(hours=8))
UTC = datetime.timezone.utc

def fetch(url):
    return subprocess.run(["curl", "-sL", "--max-time", "30", "-A", UA, url],
                          capture_output=True, text=True).stdout

def clean(raw):
    raw = re.sub(r"<script.*?</script>|<style.*?</style>", " ", raw, flags=re.S)
    raw = re.sub(r"<[^>]+>", " ", raw)
    return re.sub(r"\s+", " ", html.unescape(raw)).strip()

# 1. dates for yahoo/jefferies/jpm via bing rss
raw = fetch("https://www.bing.com/news/search?q=%E5%8F%8B%E9%82%A6+%E7%B4%94%E5%88%A9+%E5%85%A7%E5%9C%B0%E5%AE%A2&format=rss")
print("== bing dated hits ==")
for it in re.findall(r"<item>(.*?)</item>", raw, re.S):
    t = re.search(r"<title>(.*?)</title>", it, re.S)
    d = re.search(r"<pubDate>(.*?)</pubDate>", it, re.S)
    l = re.search(r"<link>(.*?)</link>", it, re.S)
    print("-", (d.group(1)[:22] if d else "?"), "|", (html.unescape(t.group(1)) if t else "")[:75])

# 2. crntt article content
raw = fetch("https://hk.crntt.com/doc/1072/2/6/3/107226380.html?coluid=7&kindid=0&docid=107226380&mdate=0822004037")
txt = clean(raw)
print("\n== CRNTT ==")
i = txt.find("友邦")
print(txt[max(0, i-100):i+1500])

# 3. IA news listing for people moves
raw = fetch("https://insuranceasia.com/insurance/news/")
print("\n== IA news listing ==")
for m in re.finditer(r'href="(https://insuranceasia\.com/insurance/news/[^"]+)"[^>]*>([^<]{15,100})<', raw):
    t2 = html.unescape(m.group(2)).strip()
    if "people" in t2.lower() or "moves" in t2.lower():
        print("-", t2[:80], "|", m.group(1))
