import re, os, email.utils, datetime
D = 'data/_raw_1010_0110'
HKT = datetime.timezone(datetime.timedelta(hours=8))
CUT = datetime.datetime(2026, 10, 8, 23, 0, tzinfo=HKT)
def parse(path):
    raw = open(path, encoding='utf-8', errors='replace').read()
    out = []
    for b in re.findall(r'<item\b.*?</item>', raw, re.S):
        def g(tag):
            m = re.search(r'<%s[^>]*>(.*?)</%s>' % (tag, tag), b, re.S)
            if not m: return ''
            s = re.sub(r'<!\[CDATA\[(.*?)\]\]>', r'\1', m.group(1), flags=re.S)
            return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', s)).strip()
        pub = g('pubDate') or g('published')
        try:
            dt = email.utils.parsedate_to_datetime(pub)
            if dt.tzinfo is None: dt = dt.replace(tzinfo=datetime.timezone.utc)
        except Exception:
            try:
                dt = datetime.datetime.fromisoformat(pub.replace('Z', '+00:00'))
            except Exception:
                dt = None
        out.append((dt, g('title'), g('link') or g('guid'), g('description')[:260]))
    return out
for f in ['ibm', 'iaasia']:
    print('#####', f)
    for dt, t, l, d in parse(os.path.join(D, f + '.out')):
        if dt and dt.astimezone(HKT) > CUT:
            print(' *', dt.astimezone(HKT).strftime('%m-%d %H:%M'), '|', t)
            print('   URL:', l)
            print('   DESC:', d)
