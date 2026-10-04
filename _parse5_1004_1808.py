import re, html

def clean(s):
    s = re.sub(r'(?is)<script.*?</script>', ' ', s)
    s = re.sub(r'(?is)<style.*?</style>', ' ', s)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()

for path, label in [('/tmp/ibm_rss.xml', 'IBM ASIA RSS'), ('/tmp/art_rss.xml', 'ARTEMIS RSS')]:
    raw = open(path, encoding='utf-8', errors='ignore').read()
    print('#' * 70)
    print('###', label, 'items:', len(re.findall(r'<item>', raw)))
    for it in re.findall(r'<item>(.*?)</item>', raw, re.S)[:14]:
        ti = re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', it, re.S)
        da = re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
        lk = re.search(r'<link>(.*?)</link>', it, re.S)
        print(' *', clean(da.group(1)) if da else '?', '|', clean(ti.group(1))[:100] if ti else '?', '|', (lk.group(1).strip() if lk else '')[:95])

for path, label in [('/tmp/fstb_it.html', 'FSTB ITALY/SWITZERLAND'), ('/tmp/gov_oct4.html', 'GOV OCT4')]:
    raw = open(path, encoding='utf-8', errors='ignore').read()
    print('#' * 70)
    print('###', label)
    c = clean(raw)
    print(c[:2200])
