import re, os, html
BASE = '/Users/leonliang/maoquanqingbao/.cache1020_1808'

for fn in ['air97221.html', 'air97220.html', 'air97259.html', 'air97257.html']:
    t = open(os.path.join(BASE, fn), encoding='utf-8', errors='ignore').read()
    print('##', fn)
    pats = re.findall(r'(\d{1,2}\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s2026)', t)
    print(' dates in raw:', sorted(set(pats))[:10])
    # find date near "AirPlus" or article info
    for m in re.finditer(r'(20\s?Oct\s?2026|19\s?Oct\s?2026|16\s?Oct\s?2026|15\s?Oct\s?2026|1[0-9]\s?Oct\s?2026)', t):
        ctx = re.sub(r'<[^>]+>', ' ', t[max(0, m.start() - 200):m.end() + 200])
        print('  ctx:', re.sub(r'\s+', ' ', ctx)[:260])
        break

print('\n\n===== insuranceasia RSS raw items =====')
rss = open(os.path.join(BASE, 'insuranceasia.xml'), encoding='utf-8', errors='ignore').read()
for m in re.finditer(r'<item[ >].*?</item>', rss, re.S):
    b = m.group(0)
    link = re.search(r'<link[^>]*>(.*?)</link>', b, re.S)
    if not link:
        continue
    u = link.group(1).strip()
    if any(k in u for k in ['sunlife-adopts', 'indonesia-insurers-face', 'taiwan-approves', 'hdfc-life', 'taiping', 'canara']):
        print('URL:', u)
        ti = re.search(r'<title[^>]*>(.*?)</title>', b, re.S)
        de = re.search(r'<description[^>]*>(.*?)</description>', b, re.S)
        pd = re.search(r'<pubDate[^>]*>(.*?)</pubDate>', b, re.S)
        print('  TITLE:', re.sub(r'<!\[CDATA\[|\]\]>', '', ti.group(1)).strip()[:120] if ti else '')
        print('  DESC:', re.sub(r'<[^>]+>', ' ', html.unescape(re.sub(r'<!\[CDATA\[|\]\]>', '', de.group(1)))).strip()[:600] if de else '')
        print('  DATE:', pd.group(1) if pd else '')
        print()
