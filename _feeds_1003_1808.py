import json, re, html
from email.utils import parsedate_to_datetime

def strip(t):
    t = re.sub(r'<[^>]+>', '', t or '')
    return html.unescape(t).strip()

def show_rss(path, label, n=15):
    raw = open(path, encoding='utf-8', errors='replace').read()
    items = re.findall(r'<item>(.*?)</item>', raw, re.S)
    if not items:
        items = re.findall(r'<entry>(.*?)</entry>', raw, re.S)
    print(f'===== {label}: {len(items)} items =====')
    for it in items[:n]:
        t = re.search(r'<title[^>]*>(.*?)</title>', it, re.S)
        l = re.search(r'<link[^>]*>(.*?)</link>', it, re.S)
        if not l:
            l = re.search(r'<link[^>]*href="([^"]+)"', it, re.S)
        d = re.search(r'<pubDate>(.*?)</pubDate>', it, re.S) or re.search(r'<published>(.*?)</published>', it, re.S) or re.search(r'<updated>(.*?)</updated>', it, re.S)
        desc = re.search(r'<description>(.*?)</description>', it, re.S) or re.search(r'<summary[^>]*>(.*?)</summary>', it, re.S)
        print('  ', strip(d.group(1) if d else '?'), '|', strip(t.group(1) if t else '?')[:90])
        print('     ', strip(l.group(1)) if l else '?')
        if desc:
            print('      ~', strip(desc.group(1))[:150])

show_rss('/tmp/ian.json', 'insuranceasianews-JSON') if False else None
try:
    posts = json.load(open('/tmp/ian.json'))
    print(f'===== insuranceasianews WP: {len(posts)} posts =====')
    for p in posts:
        print('  ', p['date'], '|', strip(p['title']['rendered'])[:90])
        print('     ', p['link'])
        print('      ~', strip(p['excerpt']['rendered'])[:150])
except Exception as e:
    print('ian.json err', e)

for path, label in [('/tmp/iaasia.xml', 'insuranceasia'), ('/tmp/artemis.xml', 'artemis'), ('/tmp/ibm.xml', 'insurancebusiness-asia')]:
    try:
        show_rss(path, label)
    except Exception as e:
        print(label, 'err', e)
