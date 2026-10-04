import re, html

def clean(s):
    s = re.sub(r'(?is)<script.*?</script>', ' ', s)
    s = re.sub(r'(?is)<style.*?</style>', ' ', s)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()

for path in ['/tmp/gmt_ia.html', '/tmp/gmt_chan.html']:
    raw = open(path, encoding='utf-8', errors='ignore').read()
    print('#' * 78)
    print('FILE', path)
    t = re.search(r'<title>(.*?)</title>', raw, re.S)
    if t:
        print('  TITLE:', clean(t.group(1))[:250])
    c = clean(raw)
    # find body start
    m = re.search(r'(insurance profits|insurance legislator|Chan Pui Leung|Insurance Authority responds)', c, re.I)
    idx = m.start() if m else 0
    print('  BODY:', c[max(0, idx-200): idx + 2600])
