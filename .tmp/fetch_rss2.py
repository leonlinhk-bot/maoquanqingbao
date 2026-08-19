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

def show_rss(name, n=15, kw=None):
    p = os.path.join(FDIR, name)
    if not os.path.exists(p):
        return
    raw = open(p, encoding='utf-8', errors='replace').read()
    items = re.findall(r'<item>(.*?)</item>', raw, re.S)
    print(f"===== {name}: {len(items)} items")
    for it in items[:n]:
        t = re.search(r'<title>(.*?)</title>', it, re.S)
        d = re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
        l = re.search(r'<link>(.*?)</link>', it, re.S)
        title = html.unescape(re.sub(r'<[^>]+>', '', t.group(1))).strip() if t else ''
        if kw and not any(k in title for k in kw):
            continue
        print('-', (d.group(1).strip()[:22] if d else '?'), '|', title[:70], '|', (l.group(1).strip()[:70] if l else '?'))

fetch("https://www.etnet.com.hk/www/tc/rss/finance.xml", "etnet_rss.xml")
fetch("https://news.mingpao.com/rss/ins/mafm.xml", "mingpao_rss.xml")
fetch("https://www.hk01.com/rss/finance", "hk01_rss.xml")
fetch("https://www.hkitalk.net/HKiTalk2/forum.php", "x.html")
show_rss("etnet_rss.xml", 20)
show_rss("mingpao_rss.xml", 20)
show_rss("hk01_rss.xml", 20)
