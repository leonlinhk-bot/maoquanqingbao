import json, re, html
raw = json.load(open('data/_raw_1003_2210.json'))

def clean(s):
    return html.unescape(re.sub('<[^>]+>', ' ', s)).strip()

def links(txt, pat, label):
    out = []
    seen = set()
    for m in re.finditer(pat, txt, re.S):
        u, t = m.group(1), clean(m.group(2))
        if u in seen or len(t) < 8:
            continue
        seen.add(u)
        out.append((t, u))
    print(f'\n===== {label} ({len(out)}) =====')
    for t, u in out[:40]:
        print(f'  {t[:100]} | {u}')

# IBM Asia breaking news
links(raw['ibm_asia']['text'], r'href="(https://www\.insurancebusinessmag\.com/asia/news/breaking-news/[^"]+)"[^>]*>(.{5,180}?)</a>', 'IBM ASIA')

# AIA
links(raw['aia_news']['text'], r'href="([^"]*press-release[^"]*)"[^>]*>(.{5,180}?)</a>', 'AIA')

# Prudential
links(raw['prudential_news']['text'], r'href="([^"]*news[^"]*)"[^>]*>(.{8,180}?)</a>', 'PRUDENTIAL')

# AXA
links(raw['axa_news']['text'], r'href="(/zh/news-room/[^"]+)"[^>]*>(.{5,180}?)</a>', 'AXA')

# SunLife
links(raw['sunlife_news']['text'], r'href="([^"]*news[^"]*)"[^>]*>(.{8,180}?)</a>', 'SUNLIFE')
