import re, html, os, json

FDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fetch')

def parse_bn(path):
    raw = open(path, encoding='utf-8', errors='replace').read()
    out = []
    # each card: <div class="news-card ..."> ... <a class="title" href="...">T</a> ... date <div class="..."...> or <span class="date">
    cards = re.findall(r'<div class="news-card[^"]*"[^>]*>(.*?)(?=<div class="news-card|$)', raw, re.S)
    for c in cards:
        t = re.search(r'class="title"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', c, re.S)
        if not t:
            t = re.search(r'<a[^>]*class="title"[^>]*>(.*?)</a>', c, re.S)
            href = ''
        else:
            href = html.unescape(t.group(1))
        title = html.unescape(re.sub(r'<[^>]+>', '', t.group(2) if t else '')).strip()
        # date: look for patterns
        d = re.search(r'(20\d\d[-/]\d{1,2}[-/]\d{1,2})', c) or re.search(r'(\d{1,2}\s+(?:min|hour|day|week)s?\s+ago)', c)
        dtxt = d.group(1) if d else ''
        src = re.search(r'class="source[^"]*"[^>]*>([^<]{2,40})<', c)
        if not title:
            continue
        out.append({'title': title, 'href': href, 'date': dtxt, 'source': html.unescape(src.group(1)).strip() if src else ''})
    return out

for f in sorted(os.listdir(FDIR)):
    if f.startswith('bn_') and f.endswith('.html'):
        items = parse_bn(os.path.join(FDIR, f))
        print(f"===== {f}: {len(items)} cards")
        for i in items[:15]:
            print('-', i['date'][:14], '|', i['source'][:20], '|', i['title'][:75])
            if i['href']:
                print('    ', i['href'][:130])
