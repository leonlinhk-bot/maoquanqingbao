import re, html
raw = open('data/_1021_1808/ibm.html', encoding='utf-8', errors='replace').read()
# 找含日期的卡片区块
for m in re.finditer(r'Oct 2[01], 2026', raw):
    seg = raw[max(0, m.start() - 1200): m.end() + 300]
    links = re.findall(r'href="(/asia/news/[^"]+)"[^>]*>(.*?)</a>', seg, re.S)
    for u, t in links[-1:]:
        t = re.sub(r'<[^>]+>', ' ', t)
        t = re.sub(r'\s+', ' ', html.unescape(t)).strip()
        if len(t) > 15:
            print(m.group(0), '|', t[:110], '|', 'https://www.insurancebusinessmag.com' + u)
