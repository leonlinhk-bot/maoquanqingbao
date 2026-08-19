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

def bingnews(q, name):
    url = "https://www.bing.com/news/search?q=" + urllib.parse.quote(q) + "&qft=sortbydate%3d%221%22"
    raw = fetch(url, name)
    if not raw:
        return
    print(f"===== {name} :: {q}")
    cards = re.findall(r'<div class="news-card[^"]*"[^>]*>(.*?)(?=<div class="news-card|$)', raw, re.S)
    for c in cards[:10]:
        t = re.search(r'class="title"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', c, re.S)
        title = html.unescape(re.sub(r'<[^>]+>', '', t.group(2))).strip() if t else ''
        href = html.unescape(t.group(1)) if t else ''
        d = re.search(r'(20\d\d[-/]\d{1,2}[-/]\d{1,2})', c) or re.search(r'(\d{1,2}\s+(?:min|hour|day|week)s?\s+ago)', c)
        src = re.search(r'class="source[^"]*"[^>]*>([^<]{2,40})<', c)
        print('-', (d.group(1) if d else '?')[:16], '|', (html.unescape(src.group(1)).strip()[:22] if src else '?'), '|', title[:70])
        if href:
            print('    ', href[:120])

for q, name in [
    ("AIA 友邦 保險 新聞", "bn2_aia.html"),
    ("Manulife 宏利 新聞", "bn2_manulife.html"),
    ("Prudential 保誠 新聞", "bn2_pru.html"),
    ("AXA 安盛 新聞", "bn2_axa.html"),
    ("Sun Life 永明 保險 新聞", "bn2_sunlife.html"),
    ("Bowtie OneDegree ZA 保險科技", "bn2_insurtechhk.html"),
    ("保險 8月20日", "bn2_0820.html"),
    ("保險公司 公告 8月20日", "bn2_ann.html"),
]:
    bingnews(q, name)
    time.sleep(0.6)

# verification fetches
print("\n===== VERIFY =====")
fetch("https://inews.hket.com/article/4178243/ant-group-acquires-fengshi-health-medical-insurance-hk", "v_ant_hket.html")
fetch("https://www.881903.com/news/local/2639898", "v_ia_881903.html")
fetch("https://www.coindesk.com/business/2026/08/18/hashkey-taps-hong-kong-s-first-regulated-stablecoin-to-settle-insurance-and-trade-dea", "v_hashkey.html")
