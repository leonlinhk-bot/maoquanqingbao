import re, html, sys

def clean(s):
    s = re.sub(r'(?is)<script.*?</script>', ' ', s)
    s = re.sub(r'(?is)<style.*?</style>', ' ', s)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()

for path in ['/tmp/ian_pru.html', '/tmp/ian_irdai.html']:
    raw = open(path, encoding='utf-8', errors='ignore').read()
    print('#' * 78)
    print('FILE', path)
    # published time
    for m in re.finditer(r'"datePublished"\s*:\s*"([^"]+)"', raw):
        print('  datePublished:', m.group(1))
    for m in re.finditer(r'(?:property|name)="(?:article:published_time|pubdate|date)"[^>]*content="([^"]+)"', raw):
        print('  meta date:', m.group(1))
    t = re.search(r'<title>(.*?)</title>', raw, re.S)
    if t:
        print('  <title>:', clean(t.group(1))[:200])
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>', raw, re.S)
    if h1:
        print('  H1:', clean(h1.group(1))[:200])
    c = clean(raw)
    # find the article body region
    idx = c.find('Japan watchdog')
    if idx < 0:
        idx = c.find('IRDAI')
    print('  BODY[0:3500]:')
    print('   ', c[max(0, idx): idx + 3500])
