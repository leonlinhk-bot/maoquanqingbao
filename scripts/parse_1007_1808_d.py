import re, os, html, json
RAW = '/Users/leonliang/maoquanqingbao/data/_raw_1007_1808'
def rd(n):
    return open(os.path.join(RAW, n), encoding='utf-8', errors='ignore').read()
def clean(s):
    s = re.sub(r'<!--.*?-->', ' ', s or '', flags=re.S)
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S)
    s = re.sub(r'<style.*?</style>', ' ', s, flags=re.S)
    return re.sub(r'\s+', ' ', s).strip()

print('=== ia_press.html raw (small?) ===')
print(rd('ia_press.html')[:1500])
print()
print('=== hkma press items ===')
t = rd('hkma_press.html')
for m in re.finditer(r'<li[^>]*>(.{0,900}?)</li>', t, re.S):
    blk = m.group(1)
    if re.search(r'\d{2} \w{3} 2026', blk):
        txt = clean(blk)
        href = re.search(r'href="([^"]+)"', blk)
        if txt:
            print(' -', txt[:160], '||', href.group(1) if href else '')
print()
print('=== ibm asia ===')
t = rd('ibm_asia.html')
for m in re.finditer(r'<a class="content-list__item__image" href="([^"]+)".{0,4000}?(\d{2} \w{3} 2026)', t, re.S):
    print(' -', m.group(2), '|', m.group(1)[:120])
