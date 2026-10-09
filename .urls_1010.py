import re, os, email.utils, datetime
D = 'data/_raw_1010_0110'
def parse(path):
    raw = open(path, encoding='utf-8', errors='replace').read()
    out = []
    for b in re.findall(r'<item\b.*?</item>', raw, re.S):
        def g(tag):
            m = re.search(r'<%s[^>]*>(.*?)</%s>' % (tag, tag), b, re.S)
            if not m: return ''
            s = re.sub(r'<!\[CDATA\[(.*?)\]\]>', r'\1', m.group(1), flags=re.S)
            return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', s)).strip()
        out.append((g('pubDate'), g('title'), g('link') or g('guid'), g('description')[:300]))
    return out
for f in ['ian_main', 'ian_hk', 'ibm', 'iaasia', 'artemis', 'scmp']:
    print('#####', f)
    for pub, t, l, d in parse(os.path.join(D, f + '.out')):
        if pub.startswith('Fri, 09 Oct 2026') or pub.startswith('Sat, 10 Oct 2026') or pub.startswith('2026-10-09') or pub.startswith('2026-10-10'):
            print(' *', pub, '|', t)
            print('   URL:', l)
            print('   DESC:', d[:220])
