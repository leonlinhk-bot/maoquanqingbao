import re, html, os, subprocess, urllib.parse

FDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fetch')
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"

def fetch(url, name, timeout=25, post=None):
    try:
        cmd = ["curl", "-sL", "--compressed", "--max-time", str(timeout), "-A", UA]
        if post:
            cmd += ["-X", "POST", "--data", post]
        cmd.append(url)
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout+10)
        open(os.path.join(FDIR, name), 'w', encoding='utf-8').write(r.stdout)
        print(f"[OK] {name} {len(r.stdout)}b")
        return r.stdout
    except Exception as e:
        print(f"[ERR] {name} {e}")
        return ""

# AIA results page from round6
raw = open(os.path.join(FDIR, 'aia_results.html'), encoding='utf-8', errors='replace').read()
t = re.search(r'<title[^>]*>(.*?)</title>', raw, re.S)
print('AIA results page title:', html.unescape(t.group(1)).strip()[:80] if t else '?', '| size', len(raw))
for m in re.finditer(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', raw, re.S):
    tt = html.unescape(re.sub(r'<[^>]+>', ' ', m.group(2))).strip()
    tt = re.sub(r'\s+', ' ', tt)
    if re.search(r'interim|2026|半年|中期', tt, re.I) and 3 < len(tt) < 100:
        print('-', tt, '|', m.group(1)[:90])

# HKEX title search for AIA 1299
post = "sortDir=0&sortByOptions=DateTime&category=0&market=SEHK&stockId=1299&documentType=-1&fromDate=20260818&toDate=20260820&title=&searchType=1&t1code=40000&t2Gcode=-2&t2code=40100&rowRange=25&lang=EN"
fetch("https://www1.hkexnews.hk/search/titleSearchServlet.do", "hkex_aia.json", post=post)
raw = open(os.path.join(FDIR, 'hkex_aia.json'), encoding='utf-8', errors='replace').read()
print('HKEX resp size:', len(raw))
for m in re.finditer(r'"title":"([^"]+)"', raw):
    print('-', m.group(1)[:80])
for m in re.finditer(r'"DATE_TIME":"([^"]+)"', raw):
    print('  at', m.group(1))
