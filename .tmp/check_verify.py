import re, html, os

FDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fetch')

def meta(path):
    raw = open(path, encoding='utf-8', errors='replace').read()
    t = re.search(r'<title[^>]*>(.*?)</title>', raw, re.S)
    d = re.search(r'<meta[^>]*name="(?:pubdate|publishdate|date|article:published_time|parsely-pub-date|datePublished)"[^>]*content="([^"]+)"', raw, re.I)
    og = re.search(r'<meta[^>]*property="article:published_time"[^>]*content="([^"]+)"', raw, re.I)
    desc = re.search(r'<meta[^>]*name="description"[^>]*content="([^"]+)"', raw, re.I)
    print('==', path)
    print('  title:', html.unescape(re.sub(r'\s+', ' ', t.group(1))).strip()[:110] if t else '?')
    if d: print('  date:', d.group(1))
    if og: print('  og-date:', og.group(1))
    if desc: print('  desc:', html.unescape(desc.group(1)).strip()[:140] if desc else '?')
    print('  size:', len(raw))

for f in ['v_ant_hket.html', 'v_ia_881903.html', 'v_hashkey.html']:
    p = os.path.join(FDIR, f)
    if os.path.exists(p):
        meta(p)
