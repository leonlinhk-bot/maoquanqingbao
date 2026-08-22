import subprocess, re, html, urllib.parse

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"

def bing_rss(q):
    url = f"https://www.bing.com/news/search?q={urllib.parse.quote(q)}&format=rss&setlang=en"
    raw = subprocess.run(["curl", "-sL", "--max-time", "20", "-A", UA, url],
                         capture_output=True, text=True).stdout
    out = []
    for it in re.findall(r"<item>(.*?)</item>", raw, re.S):
        t = re.search(r"<title>(.*?)</title>", it, re.S)
        l = re.search(r"<link>(.*?)</link>", it, re.S)
        d = re.search(r"<pubDate>(.*?)</pubDate>", it, re.S)
        out.append((d.group(1)[:25] if d else "?", html.unescape(t.group(1))[:95] if t else ""))
    return out

for q in ["site:ia.org.hk press release",
          "香港保监局 新聞稿 8月21",
          "Insurance Authority Hong Kong circular August 2026",
          "保监局 通函 8月 2026"]:
    print(f"=== {q} ===")
    try:
        for d, t in bing_rss(q)[:8]:
            print("-", d, "|", t)
    except Exception as e:
        print("ERR", e)
