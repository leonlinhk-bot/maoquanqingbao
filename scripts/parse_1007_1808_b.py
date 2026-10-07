import json, re, os, html
RAW = '/Users/leonliang/maoquanqingbao/data/_raw_1007_1808'
def rd(n):
    return open(os.path.join(RAW, n), encoding='utf-8', errors='ignore').read()
def norm(s):
    s = re.sub(r'<script.*?</script>', ' ', s or '', flags=re.S)
    s = re.sub(r'<style.*?</style>', ' ', s, flags=re.S)
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

# govhk raw head
t = rd('govhk_zh.xml')
print('=== govhk head ===')
print(t[:1200])
