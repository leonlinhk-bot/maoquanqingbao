import re, html, os, subprocess, urllib.parse

FDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fetch')
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"

def fetch(url, name, timeout=25):
    try:
        r = subprocess.run(["curl", "-sL", "--compressed", "--max-time", str(timeout), "-A", UA, url],
                           capture_output=True, text=True, timeout=timeout+10)
        open(os.path.join(FDIR, name), 'w', encoding='utf-8').write(r.stdout)
        print(f"[OK] {name} {len(r.stdout)}b")
        return r.stdout
    except Exception as e:
        print(f"[ERR] {name} {e}")
        return ""

# HKMA date context
raw = open(os.path.join(FDIR, 'hkma.html'), encoding='utf-8', errors='replace').read()
for m in re.finditer(r'.{80}2026/08/20.{80}', raw):
    print("CTX:", re.sub(r'\s+', ' ', m.group(0))[:200])
print("-----")

# Bing News sort by date
for q, name in [("香港保險", "bn_hkins.html"), ("Hong Kong insurance", "bn_hkins_en.html"),
                ("保監局", "bn_ia.html"), ("保險 友邦 OR 宏利 OR 保誠 OR 安盛 OR 永明", "bn_insurers.html"),
                ("家族辦公室 保險", "bn_family.html"), ("insurance technology Asia", "bn_insurtech.html")]:
    url = "https://www.bing.com/news/search?q=" + urllib.parse.quote(q) + "&qft=sortbydate%3d%221%22"
    raw = fetch(url, name)
    if not raw:
        continue
    print(f"== {name}")
    # news items: <a class="title" href="...">TITLE</a> with date in <div class="news-card...">
    cards = re.findall(r'<div class="news-card[^"]*"[^>]*>(.*?)</div>\s*</div>', raw, re.S)
    if not cards:
        cards = re.split(r'<div class="news-card', raw)[1:]
    for c in cards[:10]:
        t = re.search(r'class="title"[^>]*>(.*?)</a>', c, re.S)
        d = re.search(r'<div class="source[^"]*"[^>]*>.*?<span[^>]*>([^<]{4,40})</span>', c, re.S)
        h = re.search(r'href="([^"]+)"', c)
        src = re.search(r'<div class="source[^"]*"[^>]*>([^<]{2,30})', c)
        title = html.unescape(re.sub(r'<[^>]+>', '', t.group(1))).strip() if t else ''
        print('-', (d.group(1).strip() if d else '?'), '|', (src.group(1).strip() if src else '?'), '|', title[:70])
