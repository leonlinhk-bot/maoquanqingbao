import json, re, subprocess, sys, html
from datetime import datetime, timezone, timedelta
import xml.etree.ElementTree as ET

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120 Safari/537.36"
HKT = timezone(timedelta(hours=8))

def get(url, timeout=25):
    r = subprocess.run(["curl", "-m", str(timeout), "-sL", "-A", UA, url], capture_output=True, text=True, errors="replace")
    return r.stdout

def parse_rss(xml, limit=40):
    out = []
    try:
        root = ET.fromstring(xml.encode("utf-8", "replace"))
    except Exception as e:
        return [("PARSE_ERR", str(e)[:80], "", "")]
    # RSS 2.0
    for it in root.iter():
        tag = it.tag.split("}")[-1]
        if tag in ("item", "entry"):
            title = link = date = ""
            for ch in it:
                t = ch.tag.split("}")[-1]
                if t == "title":
                    title = (ch.text or "").strip()
                    if title == "" :
                        title = "".join(ch.itertext()).strip()
                elif t == "link":
                    link = (ch.text or ch.get("href") or "").strip()
                elif t in ("pubDate", "published", "updated", "date"):
                    date = (ch.text or "").strip()
            out.append((title, link, date, ""))
        if len(out) >= limit:
            break
    return out

def fmt(d):
    return d

feeds = {
    "insuranceasia": "https://insuranceasia.com/rss.xml",
    "ibm_asia": "https://www.insurancebusinessmag.com/asia/rss",
    "reinsurancenews": "https://www.reinsurancene.ws/feed/",
    "govhk": "https://www.info.gov.hk/gia/rss/general_zh.xml",
    "artemis": "https://www.artemis.bm/feed/",
}

result = {}
for k, u in feeds.items():
    body = get(u)
    items = parse_rss(body, 30)
    result[k] = items
    print("=" * 20, k, "n=", len(items), "bytes=", len(body))
    for t, l, d, _ in items[:14]:
        print(" ", d[:31], "|", html.unescape(t)[:85], "|", l[:95])

# insuranceasianews WP API
try:
    raw = get("https://insuranceasianews.com/wp-json/wp/v2/posts?per_page=25&_fields=date,link,title")
    posts = json.loads(raw)
    print("=" * 20, "ian_wp n=", len(posts))
    for p in posts[:14]:
        print(" ", p["date"], "|", html.unescape(p["title"]["rendered"])[:85], "|", p["link"][:95])
    result["ian_wp"] = posts
except Exception as e:
    print("ian_wp ERR", e)

json.dump(result, open("/tmp/feeds_1026.json", "w"), ensure_ascii=False, indent=1)
