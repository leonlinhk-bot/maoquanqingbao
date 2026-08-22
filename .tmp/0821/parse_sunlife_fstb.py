import re, html

raw = open('.tmp/0821/sunlife.html', encoding='utf-8', errors='ignore').read()
print('===== SUNLIFE news releases with dates =====')
# sunlife pages often have time tags or dates near links
for m in re.finditer(r'<a[^>]+href="(/zh-hant/about-us/newsroom/news-releases/2026/[^"]+)"[^>]*>(.*?)</a>', raw, re.S):
    href = m.group(1)
    txt = html.unescape(re.sub(r'<[^>]+>', '', m.group(2))).strip()
    txt = re.sub(r'\s+', ' ', txt)
    if len(txt) < 15:
        continue
    ctx = raw[max(0, m.start()-1200):m.start()]
    dm = re.findall(r'(20\d{2}[/.\-]\d{1,2}[/.\-]\d{1,2})', ctx)
    dm2 = re.findall(r'(\d{1,2}\s+[A-Z][a-z]{2,8}\s+20\d{2})', ctx)
    d = dm[-1] if dm else (dm2[-1] if dm2 else '')
    print(f'[{d}] {txt[:90]} -> {href[:110]}')

print()
print('===== FSTB press releases =====')
raw2 = open('.tmp/0821/fstb.html', encoding='utf-8', errors='ignore').read()
for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', raw2, re.S):
    href = m.group(1)
    txt = html.unescape(re.sub(r'<[^>]+>', '', m.group(2))).strip()
    txt = re.sub(r'\s+', ' ', txt)
    if len(txt) < 15:
        continue
    if any(k in href.lower() for k in ['press', 'news', 'pr-', 'speech', 'family']):
        ctx = raw2[max(0, m.start()-500):m.start()]
        dm = re.findall(r'(\d{1,2}\s+[A-Z][a-z]{2,8}\s+20\d{2})', ctx)
        d = dm[-1] if dm else ''
        print(f'[{d}] {txt[:80]} -> {href[:110]}')
