import re, html, os
CACHE = '/Users/leonliang/maoquanqingbao/data/_cache1005_1808/'

def txt(s):
    s = re.sub(r'<script.*?</script>|<style.*?</style>', ' ', s, flags=re.S | re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()

print('===== SCMP RSS (last 15) =====')
x = open(CACHE+'scmp_rss.xml', encoding='utf-8', errors='replace').read()
for b in re.findall(r'<item>(.*?)</item>', x, re.S)[:15]:
    t = re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', b, re.S)
    d = re.search(r'<pubDate>(.*?)</pubDate>', b, re.S)
    l = re.search(r'<link>(.*?)</link>', b, re.S)
    print('  ', (d.group(1) if d else '?').strip()[:31], '|', txt(t.group(1) if t else '')[:100])
    print('      ', (l.group(1) if l else '').strip()[:130])

print()
print('===== IAN article leads =====')
for f in ('a_ian_koreanre', 'ian_everest.html', 'ian_frag.html', 'ian_bajaj.html', 'ian_marshre.html'):
    p = CACHE + f
    if not os.path.exists(p):
        continue
    d = open(p, encoding='utf-8', errors='replace').read()
    m = re.search(r'<h1[^>]*>(.*?)</h1>', d, re.S)
    dt = re.search(r'(\w+ \d{1,2} \d{4}) by ', d)
    print('--', f, '|', dt.group(1) if dt else '?')
    print('   H1:', txt(m.group(1))[:130] if m else '?')
    # first real paragraph
    ps = [txt(p2) for p2 in re.findall(r'<p[^>]*>(.*?)</p>', d, re.S)]
    ps = [p2 for p2 in ps if len(p2) > 90 and 'To continue reading' not in p2 and 'Newsletter' not in p2]
    print('   LEAD:', (ps[0] if ps else '-')[:700])

print()
print('===== InsuranceAsia leads =====')
for f in ('a_iaasia_dc', 'iaasia_uni.html', 'iaasia_aero.html', 'iaasia_drought.html', 'iaasia_cyber.html'):
    p = CACHE + f
    if not os.path.exists(p):
        continue
    d = open(p, encoding='utf-8', errors='replace').read()
    m = re.search(r'"datePublished"\s*:\s*"([^"]+)"', d)
    m2 = re.search(r'name="description" content="([^"]{20,500})"', d)
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>', d, re.S)
    print('--', f, '|', m.group(1) if m else '?')
    print('   H1:', txt(h1.group(1))[:120] if h1 else '?')
    print('   DESC:', html.unescape(m2.group(1))[:520] if m2 else '-')
