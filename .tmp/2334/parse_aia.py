import re, html

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

# --- AIA press releases ---
raw = open('.tmp/2334/aia.html', encoding='utf-8', errors='ignore').read()
print('AIA len', len(raw))
# AIA newsroom: find article cards with dates
arts = re.findall(r'<a[^>]+href="([^"]*(?:press-release|media|news)[^"]*)"[^>]*>(.*?)</a>(.{0,400}?)', raw, re.S)
seen = set()
for u, t, after in arts:
    t = strip_tags(t)
    if not t or len(t) < 12 or u in seen: continue
    seen.add(u)
    d = find_date(after)
    print('AIA |', u[:70], '|', t[:60], '|', d)
