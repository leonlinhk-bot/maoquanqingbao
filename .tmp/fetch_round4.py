import re, html, os, subprocess, urllib.parse, time

FDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fetch')
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"

def fetch(url, name, timeout=25):
    try:
        r = subprocess.run(["curl", "-sL", "--compressed", "--max-time", str(timeout), "-A", UA, url],
                           capture_output=True, text=True, timeout=timeout+10)
        open(os.path.join(FDIR, name), 'w', encoding='utf-8').write(r.stdout)
        return r.stdout
    except Exception as e:
        print(f"[ERR] {name} {e}")
        return ""

def bingnews(q, name, n=12):
    url = "https://www.bing.com/news/search?q=" + urllib.parse.quote(q) + "&qft=sortbydate%3d%221%22"
    raw = fetch(url, name)
    if not raw:
        return
    print(f"===== {name} :: {q}")
    cards = re.findall(r'<div class="news-card[^"]*"[^>]*>(.*?)(?=<div class="news-card|$)', raw, re.S)
    for c in cards[:n]:
        t = re.search(r'class="title"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', c, re.S)
        title = html.unescape(re.sub(r'<[^>]+>', '', t.group(2))).strip() if t else ''
        href = html.unescape(t.group(1)) if t else ''
        d = re.search(r'(20\d\d[-/]\d{1,2}[-/]\d{1,2})', c) or re.search(r'(\d{1,2}\s+(?:min|hour|day|week)s?\s+ago)', c)
        src = re.search(r'class="source[^"]*"[^>]*>([^<]{2,40})<', c)
        print('-', (d.group(1) if d else '?')[:16], '|', (html.unescape(src.group(1)).strip()[:20] if src else '?'), '|', title[:68])
        if href:
            print('    ', href[:110])

bingnews("友邦保險 中期業績 新業務價值", "bn4_aia.html", 15)
time.sleep(0.6)
bingnews("AIA Group interim results 2026 new business value", "bn4_aia_en.html", 15)
time.sleep(0.6)
bingnews("保誠 業績 公布", "bn4_pru.html", 12)
