import re, os
C = 'data/_cache1006_0156'
h = open(os.path.join(C, 'ibm.html'), encoding='utf-8', errors='ignore').read()
hrefs = sorted(set(re.findall(r'href="(/asia/news/[a-z\-/]{12,}[^"]*)"', h)))
print('IBM hrefs:', len(hrefs))
for u in hrefs:
    print(u)
print('==== artemis hrefs for oct5 ====')
a = open(os.path.join(C, 'artemis.html'), encoding='utf-8', errors='ignore').read()
for m in re.finditer(r'<h2><a href="(https://www\.artemis\.bm/news/[^"]+)">(.*?)</a></h2>\s*<span class="card-subtitle">5th October 2026</span>', a, re.S):
    print(m.group(1))
print('==== hkma oct links ====')
k = open(os.path.join(C, 'hkma_press.html'), encoding='utf-8', errors='ignore').read()
for m in re.finditer(r'href="(/(?:eng|en)/news-and-media/press-releases/2026/10/[^"]+)"[^>]*>(.*?)</a>', k, re.S):
    t = re.sub(r'<[^>]+>', '', m.group(2))
    print(m.group(1), '||', re.sub(r'\s+', ' ', t).strip()[:90])
