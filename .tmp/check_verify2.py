import re, html, os

FDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fetch')

def meta(path):
    raw = open(path, encoding='utf-8', errors='replace').read()
    t = re.search(r'<title[^>]*>(.*?)</title>', raw, re.S)
    dates = re.findall(r'(?:article:published_time|datePublished|dateModified|pubdate|publishdate|parsely-pub-date|date)[^>]*content="([^"]{10,40})"', raw, re.I)
    desc = re.search(r'<meta[^>]*name="description"[^>]*content="([^"]+)"', raw, re.I)
    print('==', path)
    print('  title:', html.unescape(re.sub(r'\s+', ' ', t.group(1))).strip()[:120] if t else '?')
    seen = set()
    for d in dates:
        if d not in seen:
            seen.add(d)
            print('  date-meta:', d[:40])
    # json-ld dates
    for i, m in enumerate(re.finditer(r'"datePublished"\s*:\s*"([^"]+)"', raw)):
        if i >= 2: break
        print('  jsonld datePublished:', m.group(1))
    for i, m in enumerate(re.finditer(r'"dateModified"\s*:\s*"([^"]+)"', raw)):
        if i >= 1: break
        print('  jsonld dateModified:', m.group(1))
    if desc:
        print('  desc:', html.unescape(desc.group(1)).strip()[:150])
    # text date patterns near top
    txt = re.sub(r'<script.*?</script>', '', raw, flags=re.S)
    txt = re.sub(r'<style.*?</style>', '', txt, flags=re.S)
    txt = re.sub(r'<[^>]+>', ' ', txt)
    txt = html.unescape(re.sub(r'\s+', ' ', txt))
    for m in re.finditer(r'(20\d\d[-/]\d{1,2}[-/]\d{1,2}[T ]\d{1,2}:\d{2}[^ ]{0,8}|(?:Aug|August|Aug\.)\s+1[5-9]|(?:Aug|August|Aug\.)\s+2[0-6][, ]\s*2026|2026年8月(?:1[5-9]|2[0-6])日?)', txt):
        pass
    m = re.search(r'(published|Posted|Updated|日期|發佈)[^.]{0,40}(20\d\d[-/]\d{1,2}[-/]\d{1,2}|2026年8月\d{1,2}日|Aug(?:ust)?\.?\s+\d{1,2},?\s+2026)', txt, re.I)
    if m:
        print('  text-date:', m.group(0)[:80])
    print('  size:', len(raw))

for f in ['v_zhibao.html', 'v_manulife_ai.html', 'v_goldman_msn.html', 'v_huize.html', 'v_xceedance_gn.html']:
    p = os.path.join(FDIR, f)
    if os.path.exists(p):
        meta(p)
