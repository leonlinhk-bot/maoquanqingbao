import subprocess, re, html, urllib.parse
import xml.etree.ElementTree as ET

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120 Safari/537.36"

def get(u, t=25):
    return subprocess.run(["curl", "-m", str(t), "-sL", "-A", UA, u], capture_output=True, text=True, errors="replace").stdout

queries = [
    ("金融监管总局 保险", "zh-CN", "CN:zh-Hans"),
    ("香港 保险 大湾区", "zh-HK", "HK:zh-Hant"),
    ("insurance Hong Kong AIA Prudential", "en-US", "US:en"),
    ("友邦 保诚 宏利 安盛 香港", "zh-HK", "HK:zh-Hant"),
    ("family office Hong Kong", "en-US", "US:en"),
]
for q, hl, ceid in queries:
    url = ("https://news.google.com/rss/search?q=" + urllib.parse.quote(q)
           + "&hl=" + hl + "&gl=" + ceid.split(":")[0] + "&ceid=" + ceid)
    x = get(url)
    print("=" * 25, q)
    try:
        root = ET.fromstring(x.encode("utf-8", "replace"))
    except Exception as e:
        print(" parse err", e)
        continue
    cnt = 0
    for it in root.iter():
        if it.tag.split("}")[-1] != "item":
            continue
        title = link = date = ""
        for ch in it:
            nm = ch.tag.split("}")[-1]
            if nm == "title":
                title = (ch.text or "").strip()
            elif nm == "link":
                link = (ch.text or "").strip()
            elif nm == "pubDate":
                date = (ch.text or "").strip()
        if "25 Oct 2026" in date or "26 Oct 2026" in date:
            print("  *", date[:22], "|", html.unescape(title)[:100])
            cnt += 1
        if cnt > 8:
            break
    print("  fresh:", cnt)
