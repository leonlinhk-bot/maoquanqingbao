import json, re, subprocess, html
import xml.etree.ElementTree as ET
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120 Safari/537.36"

def get(url, timeout=30):
    r = subprocess.run(["curl", "-m", str(timeout), "-sL", "-A", UA, url], capture_output=True, text=True, errors="replace")
    return r.stdout

want = ["premium financing", "tokenised public funds", "use ai without", "state reinsurance", "captive strategy",
        "ict market leader", "infrastructure comes of age", "missing data in parametric", "acorn re"]
for feed in ["https://insuranceasia.com/rss.xml", "https://www.reinsurancene.ws/feed/", "https://www.artemis.bm/feed/"]:
    body = get(feed)
    print("==", feed)
    for m in re.finditer(r"<item>(.*?)</item>", body, flags=re.S):
        c = m.group(1)
        t = re.search(r"<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>", c, flags=re.S)
        l = re.search(r"<link>(.*?)</link>", c, flags=re.S)
        d = re.search(r"<pubDate>(.*?)</pubDate>", c, flags=re.S)
        title = html.unescape(t.group(1)) if t else ""
        link = (l.group(1) if l else "").strip()
        if any(w in title.lower() for w in want):
            print(" ", (d.group(1) if d else "")[:31], "|", title[:90])
            print("    ", link)

# SCMP rss -> find exact links
body = get("https://www.scmp.com/rss/92/feed")
print("== SCMP")
for m in re.finditer(r"<item>(.*?)</item>", body, flags=re.S):
    c = m.group(1)
    t = re.search(r"<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>", c, flags=re.S)
    l = re.search(r"<link>(.*?)</link>", c, flags=re.S)
    d = re.search(r"<pubDate>(.*?)</pubDate>", c, flags=re.S)
    title = html.unescape(t.group(1)) if t else ""
    if "premium financing" in title.lower() or "tokenised public funds" in title.lower() or "goldman" in title.lower():
        print(" ", (d.group(1) if d else "")[:31], "|", title[:90])
        print("    ", (l.group(1) if l else "").strip())

# insuranceasianews exact links
raw = get("https://insuranceasianews.com/wp-json/wp/v2/posts?per_page=12&_fields=date,link,title,excerpt")
print("== IAN")
for p in json.loads(raw):
    print(" ", p["date"], "|", html.unescape(p["title"]["rendered"])[:80])
    print("    ", p["link"])
    print("    EX:", re.sub(r"<[^>]+>", "", html.unescape(p["excerpt"]["rendered"]))[:180])
