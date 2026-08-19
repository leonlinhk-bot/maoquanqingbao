import re, html, os, subprocess, urllib.parse, time

FDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fetch')
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"

def fetch(url, name, timeout=25):
    try:
        r = subprocess.run(["curl", "-sL", "--compressed", "--max-time", str(timeout), "-A", UA, "-H", "Accept-Language: en-US,en;q=0.9,zh-HK;q=0.8", url],
                           capture_output=True, text=True, timeout=timeout+10)
        open(os.path.join(FDIR, name), 'w', encoding='utf-8').write(r.stdout)
        print(f"[OK] {name} {len(r.stdout)}b  <- {url[:100]}")
        return r.stdout
    except Exception as e:
        print(f"[ERR] {name} {e}")
        return ""

fetch("https://decrypt.co/375935/china-zhibao-bitcoin-treasury-pivot", "v_zhibao.html")
fetch("https://finance.yahoo.com/technology/ai/articles/manulife-asia-wins-best-overall-052600209.html", "v_manulife_ai.html")
fetch("https://www.msn.com/en-xl/money/personalfinance/goldman-sachs-upbeat-on-wealth-outlook-amid-market-worries-over-china-s-tighter-sc", "v_goldman_msn.html")
fetch("https://www.manilatimes.net/2026/08/10/tmt-newswire/globenewswire/huize-holding-limited-to-report-first-half-2026-financial-result", "v_huize.html")

# resolve Google News redirect for Xceedance LINE TODAY
fetch("https://news.google.com/rss/articles/CBMiZEFVX3lxTE1YWEI0YUdlekNxdW1nV3JGVHJoZTdzR2JTcHYzdmMxVGN3cUR", "v_xceedance_gn.html", 20)

# bing news for Ant Fengshi date
url = "https://www.bing.com/news/search?q=" + urllib.parse.quote("螞蟻 風石健康 收購") + "&qft=sortbydate%3d%221%22"
raw = fetch(url, "bn_ant_fengshi.html")
if raw:
    cards = re.findall(r'<div class="news-card[^"]*"[^>]*>(.*?)(?=<div class="news-card|$)', raw, re.S)
    for c in cards[:8]:
        t = re.search(r'class="title"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', c, re.S)
        title = html.unescape(re.sub(r'<[^>]+>', '', t.group(2))).strip() if t else ''
        href = html.unescape(t.group(1)) if t else ''
        d = re.search(r'(20\d\d[-/]\d{1,2}[-/]\d{1,2})', c) or re.search(r'(\d{1,2}\s+(?:min|hour|day|week)s?\s+ago)', c)
        print('-', (d.group(1) if d else '?')[:16], '|', title[:70], '|', href[:110])
