import re, subprocess, html
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120 Safari/537.36"

def get(url, timeout=30):
    r = subprocess.run(["curl", "-m", str(timeout), "-sL", "-A", UA, url], capture_output=True, text=True, errors="replace")
    return r.stdout

# --- HKMA press releases list ---
body = get("https://www.hkma.gov.hk/eng/news-and-media/press-releases/")
print("HKMA bytes", len(body))
txt = re.sub(r"<script.*?</script>", " ", body, flags=re.S)
rows = re.findall(r"(\d{1,2} \w{3} 20\d\d|\d{4}-\d{2}-\d{2})[^\n]{0,200}", txt)
# find anchors with dates
links = re.findall(r'href="([^"]*press-releases[^"]*)"[^>]*>(.*?)</a>', body, flags=re.S)
seen = set()
for href, t in links:
    t2 = html.unescape(re.sub(r"<[^>]+>", "", t)).strip()
    if not t2 or len(t2) < 12:
        continue
    if href in seen:
        continue
    seen.add(href)
    print("HKMA LINK |", t2[:110], "|", href[:110])

# --- SCMP rss with redirect ---
body2 = get("https://www.scmp.com/rss/92/feed")
print("\nSCMP bytes", len(body2))
for m in re.finditer(r"<item>(.*?)</item>", body2, flags=re.S):
    chunk = m.group(1)
    t = re.search(r"<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>", chunk, flags=re.S)
    l = re.search(r"<link>(.*?)</link>", chunk, flags=re.S)
    d = re.search(r"<pubDate>(.*?)</pubDate>", chunk, flags=re.S)
    print("SCMP |", (d.group(1) if d else "")[:31], "|", html.unescape(t.group(1) if t else "")[:95])
