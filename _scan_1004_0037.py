import json, re, html

d = json.load(open('data/_raw_1004_0037.json'))

def clean(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()

PAT = re.compile(r'(2026-10-0[34]|0[34][ /-]Oct(?:ober)?[ /-]2026|Oct(?:ober)?\.? [0-4],? 2026|2026年10月0?[34]日)')

print('=' * 70)
for key in ['insuranceasia_rss', 'govhk_zh']:
    t = d.get(key, {}).get('text', '')
    print(f'### {key}  len={len(t)}')
    # RSS: split items
    items = re.findall(r'<item>(.*?)</item>', t, re.S)
    for it in items:
        title = re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', it, re.S)
        link = re.search(r'<link>(.*?)</link>', it, re.S)
        date = re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
        ti = clean(title.group(1)) if title else ''
        da = clean(date.group(1)) if date else ''
        if PAT.search(da) or PAT.search(ti):
            print(' *', da, '|', ti[:110], '|', clean(link.group(1)) if link else '')
    print('  (total items:', len(items), ')')

print('=' * 70)
for key in ['insuranceasianews_api']:
    t = d.get(key, {}).get('text', '')
    print(f'### {key}  len={len(t)}')
    try:
        posts = json.loads(t)
    except Exception as e:
        print('  parse err', e); continue
    for p in posts:
        da = p.get('date') or p.get('modified') or ''
        ti = clean(p.get('title', {}).get('rendered', '') if isinstance(p.get('title'), dict) else str(p.get('title', '')))
        if da.startswith('2026-10-0') and da >= '2026-10-02':
            print(' *', da, '|', ti[:110], '|', p.get('link'))
    print('  (posts:', len(posts), ')')

print('=' * 70)
for key in ['ibm_asia', 'artemis', 'hkma_press', 'prudential_news', 'axa_news', 'sunlife_news', 'nfra', 'scmp_insurance']:
    t = d.get(key, {}).get('text', '')
    print(f'### {key}  len={len(t)}')
    # find matches with context
    n = 0
    for m in PAT.finditer(t):
        seg = t[max(0, m.start() - 300): m.start() + 300]
        seg = clean(seg)
        print('  ~', m.group(0), '::', seg[:260])
        n += 1
        if n >= 12:
            print('  ...(more)')
            break
    if n == 0:
        print('  (no date matches)')
