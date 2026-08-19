import re, html, subprocess, urllib.parse, sys, datetime

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"

def gnews(q, hl="zh-HK", gl="HK", n=15):
    url = f"https://news.google.com/rss/search?q={urllib.parse.quote(q)}&hl={hl}&gl={gl}&ceid={gl}:{hl}"
    raw = subprocess.run(["curl", "-sL", "--max-time", "25", "-A", UA, url],
                         capture_output=True, text=True).stdout
    items = re.findall(r"<item>(.*?)</item>", raw, re.S)
    out = []
    for it in items:
        t = re.search(r"<title>(.*?)</title>", it, re.S)
        l = re.search(r"<link>(.*?)</link>", it, re.S)
        d = re.search(r"<pubDate>(.*?)</pubDate>", it, re.S)
        s = re.search(r"<source[^>]*>(.*?)</source>", it, re.S)
        out.append({
            "title": html.unescape(t.group(1)) if t else "",
            "link": html.unescape(l.group(1)) if l else "",
            "pubDate": d.group(1) if d else "",
            "source": html.unescape(s.group(1)) if s else ""
        })
    return out

q = sys.argv[1] if len(sys.argv) > 1 else "香港保險"
res = gnews(q)
print(f"=== GN {q}: {len(res)} items ===")
for r in res[:12]:
    print("-", r["pubDate"][:22], "|", r["source"][:20], "|", r["title"][:90])
    print("  ", r["link"][:150])
