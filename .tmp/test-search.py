import re, html, subprocess, urllib.parse, sys

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"

def fetch(url):
    return subprocess.run(["curl", "-sL", "--max-time", "25", "-A", UA, url],
                          capture_output=True, text=True).stdout

def bing(q, n=8):
    raw = fetch("https://www.bing.com/search?q=" + urllib.parse.quote(q) + "&count=" + str(n) + "&setlang=en")
    out = []
    # try new structure: <li class="b_algo"> ... <h2><a href="URL" ...>TITLE</a></h2>
    for m in re.finditer(r'<h2[^>]*><a[^>]*href="([^"]+)"[^>]*>(.*?)</a></h2>', raw, re.S):
        url = html.unescape(m.group(1))
        title = re.sub(r"<[^>]+>", "", m.group(2))
        title = html.unescape(title).strip()
        if title and url.startswith("http"):
            out.append((title, url))
    return out, len(raw)

def ddg(q, n=8):
    raw = fetch("https://html.duckduckgo.com/html/?q=" + urllib.parse.quote(q))
    out = []
    for m in re.finditer(r'class="result__a"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', raw, re.S):
        url = html.unescape(m.group(1))
        if url.startswith("//duckduckgo.com/l/?uddg="):
            url = urllib.parse.unquote(url.split("uddg=")[1].split("&rut=")[0])
        title = re.sub(r"<[^>]+>", "", m.group(2))
        out.append((html.unescape(title).strip(), url))
    return out, len(raw)

q = sys.argv[1] if len(sys.argv) > 1 else "Hong Kong insurance regulator news August 2026"
print("=== BING ===")
try:
    res, ln = bing(q)
    print(f"(raw {ln}b, {len(res)} parsed)")
    for t,u in res[:8]: print("-", t[:100], "\n  ", u[:160])
except Exception as e: print("ERR", e)
print("=== DDG ===")
try:
    res, ln = ddg(q)
    print(f"(raw {ln}b, {len(res)} parsed)")
    for t,u in res[:8]: print("-", t[:100], "\n  ", u[:160])
except Exception as e: print("ERR", e)
