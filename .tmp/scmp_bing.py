import subprocess, re, html, urllib.parse

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"

def fetch(url):
    return subprocess.run(["curl", "-sL", "--max-time", "25", "-A", UA, url],
                          capture_output=True, text=True).stdout

q = "Ping An eyes Hong Kong ETFs after nod on cross-border investment"
url = f"https://www.bing.com/news/search?q={urllib.parse.quote(q)}&format=rss"
raw = fetch(url)
for it in re.findall(r"<item>(.*?)</item>", raw, re.S):
    t = re.search(r"<title>(.*?)</title>", it, re.S)
    l = re.search(r"<link>(.*?)</link>", it, re.S)
    print("TITLE:", html.unescape(t.group(1))[:100] if t else "")
    print("LINK:", html.unescape(l.group(1))[:160] if l else "")
    link = html.unescape(l.group(1)) if l else ""
    if "apiclick" in link:
        real = subprocess.run(["curl", "-sL", "--max-time", "25", "-A", UA, "-o", "/dev/null", "-w", "%{url_effective}", link],
                              capture_output=True, text=True).stdout
        print("REAL:", real[:160])
    print("---")
