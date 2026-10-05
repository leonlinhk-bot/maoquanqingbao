import json, re, html, os
import xml.etree.ElementTree as ET

C = 'data/_cache1006_0156'

def clean(s):
    s = re.sub(r'<[^>]+>', '', s or '')
    return html.unescape(s).strip()

def rss(name, path, limit=30):
    p = os.path.join(C, path)
    if not os.path.exists(p):
        print('MISSING', name); return
    try:
        t = ET.parse(p)
    except Exception as e:
        print('FAIL', name, e); return
    print('=' * 72)
    print('RSS', name)
    n = 0
    for it in t.getroot().iter('item'):
        ti = clean(it.findtext('title') or '')
        li = (it.findtext('link') or '').strip()
        pd = (it.findtext('pubDate') or '').strip()
        src = clean(it.findtext('source') or '')
        print('  ', pd[:31], '|', ti[:88], '|', src[:18])
        n += 1
        if n >= limit:
            break

for f in ['gn_ia.xml', 'gn_ia_zh.xml', 'gn_hk_ins.xml', 'gn_fam.xml', 'gn_insurtech.xml', 'gn_manulife.xml']:
    rss(f, f, 22)

# govhk: filter insurance-related
print('=' * 72)
print('GOVHK insurance-related (last 100)')
h = open(os.path.join(C, 'govhk_zh.xml'), encoding='utf-8', errors='ignore').read()
kw = ['保險', '保監', '理賠', '強積金', '年金', '退休', '財經事務及庫務局', '家族辦公室', '基金']
for m in re.finditer(r'<item>(.*?)</item>', h, re.S):
    blk = m.group(1)
    ti = clean(re.search(r'<title>(.*?)</title>', blk, re.S).group(1))
    pd = clean(re.search(r'<pubDate>(.*?)</pubDate>', blk, re.S).group(1))
    li = clean(re.search(r'<link>(.*?)</link>', blk, re.S).group(1))
    if any(k in ti for k in kw):
        print('  ', pd[:31], '|', ti[:90], '|', li[:80])

# nfra
print('=' * 72)
print('NFRA page text sample')
n = open(os.path.join(C, 'nfra.html'), encoding='utf-8', errors='ignore').read()
txt = re.sub(r'<script.*?</script>', ' ', n, flags=re.S)
txt = re.sub(r'<style.*?</style>', ' ', txt, flags=re.S)
txt = clean(txt)
txt = re.sub(r'\s+', ' ', txt)
print(txt[:2500])
