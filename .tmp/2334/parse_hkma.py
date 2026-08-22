import re, html, json

def strip_tags(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<style.*?</style>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

# HKMA press releases: look for date + title patterns
raw = open('.tmp/2334/hkma.html', encoding='utf-8', errors='ignore').read()
print('HKMA len', len(raw))
# find links with dates
# typical HKMA structure: <li><a href="/eng/news-and-media/press-releases/2026/08/20260821_1_eng_1.htm">Title</a><p>21 Aug 2026</p></li>
items = re.findall(r'<a href="(/eng/news-and-media/press-releases/\d{4}/\d{2}/[^"]+)"[^>]*>(.*?)</a>', raw, flags=re.S)
print('hkma link count:', len(items))
for u, t in items[:40]:
    print(u, '|', strip_tags(t)[:90])
