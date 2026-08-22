import re, html

def strip_tags(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

raw = open('data/_raw/t0822c/hkma-press.html', encoding='utf-8', errors='ignore').read()
# pattern: <a href=".../2026/08/2026082X-Y/" title="TITLE">TITLE DATE</a>
pat = re.compile(r'<a href="(/eng/news-and-media/press-releases/2026/08/202608\d+-\d+/)" title="([^"]+)"[^>]*>(.*?)</a>', re.S)
seen = set()
for m in pat.finditer(raw):
    url, title, body = m.group(1), m.group(2), strip_tags(m.group(3))
    if url in seen:
        continue
    seen.add(url)
    print(f'{title[:70]} | {body[:50]} | https://www.hkma.gov.hk{url}')
