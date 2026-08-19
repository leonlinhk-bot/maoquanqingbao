import re, html, os, subprocess, urllib.parse

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

def gn(q, hl='en'):
    name = 'g5_' + re.sub(r'[^a-zA-Z0-9]+', '_', q)[:40] + '.xml'
    ceid = 'HK:zh-Hant' if hl == 'zh-HK' else 'HK:en'
    url = "https://news.google.com/rss/search?q=" + urllib.parse.quote(q) + "&hl=" + hl + "&gl=HK&ceid=" + ceid
    raw = fetch(url, name)
    if not raw:
        return
    items = re.findall(r'<item>(.*?)</item>', raw, re.S)
    print(f"===== {q} ({len(items)} items)")
    for it in items[:12]:
        t = re.search(r'<title>(.*?)</title>', it, re.S)
        d = re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
        s = re.search(r'<source[^>]*>(.*?)</source>', it, re.S)
        l = re.search(r'<link>(.*?)</link>', it, re.S)
        print('-', d.group(1).strip()[:25] if d else '?', '|', html.unescape(re.sub(r'<[^>]+>', '', t.group(1))).strip()[:68] if t else '?', '|', html.unescape(s.group(1)).strip()[:20] if s else '?')

# AIA results page
fetch("https://www.aia.com/en/investor-relations/overview/results-presentations", "aia_results.html")

# Goldman full title from cached bing news
raw = open(os.path.join(FDIR, 'bn_hkins_en.html'), encoding='utf-8', errors='replace').read()
i = raw.find('Goldman Sachs upbeat')
if i > 0:
    seg = raw[max(0, i-3000):i+500]
    t = re.search(r'class="title"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', seg, re.S)
    print('\nGOLDMAN:', html.unescape(re.sub(r'<[^>]+>', '', t.group(2))).strip() if t else '?')
    print('URL:', html.unescape(t.group(1)) if t else '?')
else:
    print('goldman title not found in bn_hkins_en')

gn('AIA when:2d')
gn('友邦保險 when:2d', 'zh-HK')
gn('保險 when:1d', 'zh-HK')
