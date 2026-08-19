import re, html, subprocess, urllib.parse
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
def search(q, n=8):
    raw = subprocess.run(["curl", "-sL", "--max-time", "25", "-A", UA,
                          "https://www.bing.com/search?q=" + urllib.parse.quote(q) + "&count=" + str(n) + "&mkt=en-HK"],
                         capture_output=True, text=True).stdout
    out = []
    for m in re.finditer(r'<h2[^>]*><a[^>]*href="([^"]+)"[^>]*>(.*?)</a></h2>', raw, re.S):
        url = html.unescape(m.group(1))
        if url.startswith("https://www.bing.com/ck/a"):
            # extract the real url from the redirect target
            mm = re.search(r'&u=a1aHR0c[^&"]+', url)
            if mm:
                import base64
                try:
                    b64 = mm.group(0)[3:]
                    b64 += "=" * (-len(b64) % 4)
                    url = base64.urlsafe_b64decode(b64).decode()
                except Exception:
                    url = url
        title = re.sub(r"<[^>]+>", "", m.group(2))
        out.append((html.unescape(title).strip(), url))
    return out
for q in ["Marco Capital Pro Global insurance acquisition", "Marco Capital 收購 Pro Global 保險"]:
    print("###", q)
    for t, u in search(q)[:6]:
        print("-", t[:100])
        print("  ", u[:170])
