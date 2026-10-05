import re, html, os
C = 'data/_cache1006_0156'
def clean(s):
    return html.unescape(re.sub(r'<[^>]+>', '', s or '')).strip()

a = open(os.path.join(C, 'artemis.html'), encoding='utf-8', errors='ignore').read()
print('===== ARTEMIS rows w/ card-subtitle dates =====')
for m in re.finditer(r'<h2><a href="(https://www\.artemis\.bm/news/[^"]+)">(.*?)</a></h2>\s*<span class="card-subtitle">(.*?)</span>', a, re.S):
    print(clean(m.group(3)), '|', clean(m.group(2))[:90], '|', m.group(1)[:75])

s = open(os.path.join(C, 'sunlife.html'), encoding='utf-8', errors='ignore').read()
print('===== SUNLIFE near-title date hunt =====')
for m in re.finditer(r'href="(/zh-hant/about-us/newsroom/news-releases/2026/[^"]+)"[^>]*>(.*?)</a>(.{0,600}?)(\d{1,2}\s+\w+\s+2026|2026[年\-/]\d{1,2}[月\-/]\d{1,2}|\d{1,2}\s+\w+,?\s+2026)', s, re.S):
    print(clean(m.group(2))[:80], '||', clean(m.group(4)))
print('--- sunlife raw date tokens ---')
print(sorted(set(re.findall(r'\b\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\w*\s*,?\s*2026', s)))[:25])
print(sorted(set(re.findall(r'2026[年\-/]\d{1,2}[月\-/]\d{1,2}', s)))[:25])
