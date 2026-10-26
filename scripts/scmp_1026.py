import subprocess, re, html
import xml.etree.ElementTree as ET

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120 Safari/537.36"
u = "https://www.scmp.com/rss/92/feed"
t = subprocess.run(["curl", "-m", "25", "-sL", "-A", UA, u], capture_output=True, text=True, errors="replace").stdout
root = ET.fromstring(t.encode("utf-8", "replace"))
for it in root.iter():
    if it.tag.split("}")[-1] != "item":
        continue
    title = link = date = desc = ""
    for ch in it:
        n = ch.tag.split("}")[-1]
        if n == "title":
            title = (ch.text or "").strip()
        elif n == "link":
            link = (ch.text or "").strip()
        elif n == "pubDate":
            date = (ch.text or "").strip()
        elif n == "description":
            desc = re.sub(r"<[^>]+>", "", html.unescape(ch.text or ""))[:120]
    if "2026/10/25" in date or "2026/10/26" in date or "25 Oct 2026" in date or "26 Oct 2026" in date:
        print(date, "|", html.unescape(title)[:90])
        print("   ", link)
        print("   ", desc)
