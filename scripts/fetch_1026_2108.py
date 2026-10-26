import json, re, subprocess, html
import xml.etree.ElementTree as ET

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120 Safari/537.36"

def get(url, timeout=25):
    r = subprocess.run(["curl", "-m", str(timeout), "-sL", "-A", UA, url], capture_output=True, text=True, errors="replace")
    return r.stdout

def parse_rss(xml, limit=30):
    out = []
    try:
        root = ET.fromstring(xml.encode("utf-8", "replace"))
    except Exception as e:
        return [("PARSE_ERR", str(e)[:80], "", "")]
    for it in root.iter():
        tag = it.tag.split("}")[-1]
        if tag in ("item", "entry"):
            title = link = date = desc = ""
            for ch in it:
                t = ch.tag.split("}")[-1]
                if t == "title":
                    title = (ch.text or "".join(ch.itertext()) or "").strip()
                elif t == "link":
                    link = (ch.text or ch.get("href") or "").strip()
                elif t in ("pubDate", "published", "updated", "date"):
                    date = (ch.text or "").strip()
                elif t in ("description", "summary"):
                    desc = (ch.text or "")[:200]
            out.append((title, link, date, desc))
        if len(out) >= limit:
            break
    return out

feeds = {
    "insuranceasia": "https://insuranceasia.com/rss.xml",
    "ibm_asia": "https://www.insurancebusinessmag.com/asia/rss",
    "reinsurancenews": "https://www.reinsurancene.ws/feed/",
    "artemis": "https://www.artemis.bm/feed/",
    "govhk": "https://www.info.gov.hk/gia/rss/general_zh.xml",
}

for k, u in feeds.items():
    body = get(u)
    items = parse_rss(body, 30)
    print("=" * 22, k, "n=", len(items), "bytes=", len(body))
    for t, l, d, _ in items[:12]:
        print(" ", d[:31], "|", html.unescape(t)[:92], "|", l[:100])

# insuranceasianews WP API
try:
    raw = get("https://insuranceasianews.com/wp-json/wp/v2/posts?per_page=20&_fields=date,link,title")
    arr = json.loads(raw)
    print("=" * 22, "insuranceasianews", "n=", len(arr))
    for p in arr:
        print(" ", p["date"], "|", html.unescape(p["title"]["rendered"])[:92], "|", p["link"][:100])
except Exception as e:
    print("IAN_ERR", e)
