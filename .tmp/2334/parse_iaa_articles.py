import re, html, glob

def strip_tags(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<style.*?</style>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

MONTHS = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}

def find_date(raw):
    m = re.search(r'(20\d{2}-\d{2}-\d{2}[T ]\d{2}:\d{2}(?::\d{2})?)', raw)
    if m: return m.group(1)
    m = re.search(r'(\d{1,2})\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+(20\d{2})', raw)
    if m: return f"{m.group(3)}-{MONTHS[m.group(2)]:02d}-{int(m.group(1)):02d}"
    return None

for fn in sorted(glob.glob('.tmp/2334/iaa_*.html')):
    raw = open(fn, encoding='utf-8', errors='ignore').read()
    title = re.search(r'<title>(.*?)</title>', raw, re.S)
    d = find_date(raw)
    meta = re.search(r'<meta[^>]+(?:property="article:published_time"|name="date")[^>]+content="([^"]+)"', raw)
    print(fn.split('/')[-1][:55], '|', strip_tags(title.group(1))[:55] if title else '?', '|', d, '|', meta.group(1) if meta else '')
