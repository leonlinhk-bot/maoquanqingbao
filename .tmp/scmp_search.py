import subprocess, re, html, urllib.parse

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"

def fetch(url):
    return subprocess.run(["curl", "-sL", "--max-time", "25", "-A", UA, url],
                          capture_output=True, text=True).stdout

q = urllib.parse.quote("Ping An eyes Hong Kong ETFs")
raw = fetch(f"https://www.scmp.com/search?query={q}")
print("len:", len(raw))
for m in re.finditer(r'href="(https://www\.scmp\.com/business[^"]+)"', raw):
    u = m.group(1)
    if "search" not in u and "article" in u:
        print("ART:", u[:150])
# sitemap approach
raw2 = fetch("https://www.scmp.com/sitemap.xml")
print("sitemap len:", len(raw2))
