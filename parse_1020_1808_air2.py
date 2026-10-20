import re, os, html
BASE = '/Users/leonliang/maoquanqingbao/.cache1020_1808'
p = os.path.join(BASE, 'iaasia.html')
t = open(p, encoding='utf-8', errors='ignore').read()
t = re.sub(r'<script.*?</script>', ' ', t, flags=re.S | re.I)
# locate each article link, then look backwards up to 600 chars for a date
for m in re.finditer(r'<a[^>]+href="(/News/View-NewsLetter-Article/id/\d+/[^"]*)"[^>]*>(.*?)</a>', t, re.S):
    href, inner = m.group(1), m.group(2)
    txt = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', inner))).strip()
    if len(txt) < 25:
        continue
    back = t[max(0, m.start() - 800):m.start()]
    back_txt = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', back)))
    dates = re.findall(r'\d{1,2}\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s2026', back_txt)
    ahead = t[m.end():m.end() + 800]
    ahead_txt = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', ahead)))
    dates2 = re.findall(r'\d{1,2}\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s2026', ahead_txt)
    print((dates[-1] if dates else (dates2[0] if dates2 else '??')).ljust(13), '|', txt[:100])
    print('     https://www.asiainsurancereview.com' + href.split('?')[0])
