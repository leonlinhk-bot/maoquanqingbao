import re, subprocess, html, json, sys

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120 Safari/537.36"

def get(u):
    r = subprocess.run(["curl", "-m", "30", "-sL", "-A", UA, u], capture_output=True, text=True, errors="replace")
    return r.stdout

# HKMA press releases
t = get("https://www.hkma.gov.hk/eng/news-and-media/press-releases/")
print("=== HKMA bytes", len(t))
seen = []
for m in re.finditer(r'href="(/eng/news-and-media/press-releases/2026/1[01]/[^"]+)"[^>]*>(.*?)</a>', t, re.S):
    url, txt = m.group(1), re.sub(r"<[^>]+>", "", m.group(2)).strip()
    if (url, txt) in seen:
        continue
    seen.append((url, txt))
print("links:", len(seen))
for u, x in seen[:25]:
    print(" ", u, "|", html.unescape(x)[:90])
