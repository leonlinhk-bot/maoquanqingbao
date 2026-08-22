import re, html

def strip_tags(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

# FSTB press page - inspect structure
raw = open('data/_raw/t0822c/fstb-press.html', encoding='utf-8', errors='ignore').read()
print('FSTB size:', len(raw))
# look for any links
links = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', raw, re.S | re.I)
cnt = 0
for u, t in links:
    t = strip_tags(t)
    if not t or len(t) < 8:
        continue
    if any(skip in u for skip in ['.css', '.js', '.png', '.jpg', '.ico', 'javascript']):
        continue
    cnt += 1
    if cnt <= 40:
        print(f'  {t[:80]} | {u[:110]}')
print('total links:', cnt)
