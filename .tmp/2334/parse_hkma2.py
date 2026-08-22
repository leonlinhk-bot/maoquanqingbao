import re, html, json

def strip_tags(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<style.*?</style>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

# HKMA: full item list with dates
raw = open('.tmp/2334/hkma.html', encoding='utf-8', errors='ignore').read()
# HKMA structure: <a href="...">TITLE</a> ... <p>21 Aug 2026</p> or date in <span>
# search for pattern of li blocks
blocks = re.findall(r'<li[^>]*>(.*?)</li>', raw, flags=re.S)
print('hkma li blocks:', len(blocks))
for b in blocks:
    m = re.search(r'href="(/eng/news-and-media/press-releases/[^"]+)"', b)
    if not m: continue
    t = strip_tags(re.sub(r'<a[^>]*>.*?</a>', ' ', b))
    d = re.findall(r'(\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{4})', b)
    print(m.group(1).split('/')[-1], '|', t[:70], '|', d[:1])
