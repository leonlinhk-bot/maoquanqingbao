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

def gn(q, name=None, hl='en', gl='HK'):
    if name is None:
        name = 'g_' + re.sub(r'[^a-zA-Z0-9]+', '_', q)[:40] + '.xml'
    else:
        name = name + '.xml'
    url = "https://news.google.com/rss/search?q=" + urllib.parse.quote(q) + "&hl=" + hl + "&gl=" + gl + "&ceid=HK:en"
    raw = fetch(url, name)
    if not raw:
        return
    items = re.findall(r'<item>(.*?)</item>', raw, re.S)
    print(f"===== {name} :: {q} ({len(items)} items)")
    for it in items[:12]:
        t = re.search(r'<title>(.*?)</title>', it, re.S)
        d = re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
        s = re.search(r'<source[^>]*>(.*?)</source>', it, re.S)
        l = re.search(r'<link>(.*?)</link>', it, re.S)
        print('-', d.group(1).strip()[:25] if d else '?', '|', html.unescape(re.sub(r'<[^>]+>', '', t.group(1))).strip()[:70] if t else '?', '|', html.unescape(s.group(1)).strip()[:22] if s else '?', '|', (l.group(1).strip()[:60] if l else '?'))

gn('AIA results when:1d')
gn('"AIA" "new business value" when:2d')
gn('AIA 中期業績 when:1d', 'zh-HK')
gn('友邦 when:1d', 'zh-HK')

# AIA group IR page
fetch("https://www.aia.com/en/about-aia/investor-relations/results-and-reports", "aia_ir.html")
