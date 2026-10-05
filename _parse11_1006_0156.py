import re, html, os
C = 'data/_cache1006_0156'
def clean(s):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', s or ''))).strip()

c = open(os.path.join(C, 'corgi1.html'), encoding='utf-8', errors='ignore').read()
m = re.search(r'<article.*?</article>', c, re.S) or re.search(r'entry-content(.{0,6000})', c, re.S)
print('=== CORGI body ===')
print(clean(m.group(0))[:1400] if m else 'n/a')

f = open(os.path.join(C, 'famoff.html'), encoding='utf-8', errors='ignore').read()
print('=== FAMILYOFFICEHK titles ===')
for m in re.finditer(r'<h[23][^>]*>(.*?)</h[23]>', f, re.S):
    t = clean(m.group(1))
    if len(t) > 4:
        print('  ', t[:100])
print('=== FAMILYOFFICEHK date tokens ===')
print(sorted(set(re.findall(r'\b\d{1,2}\s+\w{3,9},?\s+2026', f)))[:20])
print('=== govhk 財經事務 / 保監 (last 60 items) ===')
g = open(os.path.join(C, 'govhk_zh.xml'), encoding='utf-8', errors='ignore').read()
for m in re.finditer(r'<item>(.*?)</item>', g, re.S):
    b = m.group(1)
    t = clean(re.search(r'<title>(.*?)</title>', b, re.S).group(1))
    d = clean(re.search(r'<pubDate>(.*?)</pubDate>', b, re.S).group(1))
    l = clean(re.search(r'<link>(.*?)</link>', b, re.S).group(1))
    if any(k in t for k in ['保險', '保監', '財經', '稅', '投資推廣', '家族', '強積金', '退休', '金融']):
        print('  *', d[:31], '|', t[:90], '|', l[:70])
