import re, html, os, json, datetime, subprocess, urllib.parse

FDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fetch')

# ---- HKMA press releases page ----
raw = open(os.path.join(FDIR, 'hkma.html'), encoding='utf-8', errors='replace').read()
# find article blocks
blocks = re.findall(r'<a[^>]*href="([^"]*press-releases[^"]*)"[^>]*>(.*?)</a>', raw, re.S)
print("HKMA link blocks:", len(blocks))
seen = set()
for href, txt in blocks:
    t = html.unescape(re.sub(r'<[^>]+>', ' ', txt)).strip()
    t = re.sub(r'\s+', ' ', t)
    if not t or href in seen:
        continue
    seen.add(href)
    print('-', t[:80], '|', href[:110])

# dates near items
print("\n--- HKMA date strings ---")
for m in re.finditer(r'(20(25|26)/(0[0-9]|1[0-2])/([0-2][0-9]|3[01]))[^<]{0,20}', raw):
    pass
dates = re.findall(r'2026/08/2[0-9]', raw)
print("dates found:", sorted(set(dates)))

# ---- InsuranceAsia cached feed ----
print("\n--- InsuranceAsia ia-rss2.xml (cached 00:57) ---")
raw2 = open('/Users/leonliang/maoquanqingbao/.tmp/ia-rss2.xml', encoding='utf-8', errors='replace').read()
for it in re.findall(r'<item>(.*?)</item>', raw2, re.S)[:15]:
    t = re.search(r'<title>(.*?)</title>', it, re.S)
    d = re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
    l = re.search(r'<link>(.*?)</link>', it, re.S)
    print('-', d.group(1).strip() if d else '?', '|', html.unescape(re.sub(r'<[^>]+>','',t.group(1))).strip()[:70] if t else '?', '|', l.group(1).strip()[:80] if l else '?')

# ---- fresh Google News with when:6h and when:1d ----
def gn(q, name, hl='zh-HK'):
    url = "https://news.google.com/rss/search?q=" + urllib.parse.quote(q) + "&hl=" + hl + "&gl=HK&ceid=HK:zh-Hant"
    r = subprocess.run(["curl", "-sL", "--compressed", "--max-time", "20", "-A", "Mozilla/5.0", url],
                       capture_output=True, text=True, timeout=30)
    open(os.path.join(FDIR, name), 'w', encoding='utf-8').write(r.stdout)
    items = re.findall(r'<item>(.*?)</item>', r.stdout, re.S)
    print(f"\n=== {name} ({q}) {len(items)} items ===")
    for it in items[:12]:
        t = re.search(r'<title>(.*?)</title>', it, re.S)
        d = re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
        s = re.search(r'<source[^>]*>(.*?)</source>', it, re.S)
        l = re.search(r'<link>(.*?)</link>', it, re.S)
        print('-', d.group(1).strip()[:25] if d else '?', '|', html.unescape(re.sub(r'<[^>]+>','',t.group(1))).strip()[:65] if t else '?', '|', html.unescape(s.group(1)).strip()[:25] if s else '?')

gn('香港保險 when:6h', 'g6_hkins.xml')
gn('香港保險 when:1d', 'g1d_hkins.xml')
gn('Hong Kong insurance when:1d', 'g1d_en_hkins.xml', 'en')
gn('保監局 when:1d', 'g1d_ia.xml')
