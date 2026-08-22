import re, html

def strip_tags(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<style.*?</style>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

raw = open('.tmp/2334/hkma.html', encoding='utf-8', errors='ignore').read()
# try alternative: find all <a href="/eng/news-and-media/press-releases/..."> and surrounding text
pat = re.compile(r'<a[^>]+href="(/eng/news-and-media/press-releases/[^"]+)"[^>]*>(.*?)</a>', re.S)
for m in pat.finditer(raw):
    u, t = m.group(1), strip_tags(m.group(2))
    if not t: continue
    # grab 300 chars after the anchor for date
    after = raw[m.end():m.end()+400]
    d = re.findall(r'(\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{4})', after)
    print(u.split('/')[-1], '|', t[:80], '|', d[:1])
