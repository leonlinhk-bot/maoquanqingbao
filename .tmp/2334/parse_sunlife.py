import re, html

def strip_tags(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<style.*?</style>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

MONTHS = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}

# SUNLIFE news releases 2026 - full listing with dates
raw = open('.tmp/2334/sunlife.html', encoding='utf-8', errors='ignore').read()
# find news-release cards
for m in re.finditer(r'<a[^>]+href="(/en/about-us/newsroom/news-releases/2026/[^"]+)"[^>]*>(.*?)</a>(.{0,700}?)', raw, re.S):
    u, t = m.group(1), strip_tags(m.group(2))
    if not t: continue
    after = m.group(3)
    d = re.findall(r'(\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+20\d{2}|\d{4}-\d{2}-\d{2})', after)
    print('SL |', u.split('/')[-1][:60], '|', t[:60], '|', d[:1])
