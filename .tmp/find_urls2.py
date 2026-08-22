import subprocess, re, html, urllib.parse

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"

def fetch(url):
    return subprocess.run(["curl", "-sL", "--max-time", "25", "-A", UA, url],
                          capture_output=True, text=True).stdout

def bing(q):
    raw = fetch(f"https://www.bing.com/news/search?q={urllib.parse.quote(q)}&format=rss")
    for it in re.findall(r"<item>(.*?)</item>", raw, re.S):
        t = re.search(r"<title>(.*?)</title>", it, re.S)
        l = re.search(r"<link>(.*?)</link>", it, re.S)
        link = html.unescape(l.group(1)) if l else ""
        print("-", (html.unescape(t.group(1)) if t else "")[:80])
        if "apiclick" in link:
            real = subprocess.run(["curl", "-sL", "--max-time", "25", "-A", UA, "-o", "/dev/null", "-w", "%{url_effective}", link],
                                  capture_output=True, text=True).stdout
            print("  REAL:", real[:150])

def ddg(q):
    raw = fetch(f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(q)}")
    for m in re.finditer(r'class="result__a"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', raw, re.S):
        u = html.unescape(m.group(1))
        t = re.sub(r"<[^>]+>", "", m.group(2)).strip()
        if "uddg=" in u:
            u = urllib.parse.unquote(u.split("uddg=")[1].split("&")[0])
        print("-", t[:80], "|", u[:130])

print("== bing: 友邦 純利 內地客 ==")
bing("友邦 半年純利 內地客 投保")
print("== bing: site:insuranceasia.com people moves ==")
bing("site:insuranceasia.com insurance people moves week")
print("== ddg: 友邦 半年純利大增 ==")
ddg("友邦 半年純利大增 內地客投保需求")
print("== ddg: insuranceasia people moves ==")
ddg("insuranceasia Aon Zurich Marsh AIG people moves week")
