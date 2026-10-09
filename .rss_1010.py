import re, json, email.utils, datetime, os, io, sys

D = 'data/_raw_1010_0110'
CUT = datetime.datetime(2026, 10, 8, 23, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=8)))

def hkt(dt):
    return dt.astimezone(datetime.timezone(datetime.timedelta(hours=8)))

def parse_rss(path, maxn=40):
    raw = open(path, encoding='utf-8', errors='replace').read()
    out = []
    blocks = re.findall(r'<item\b.*?</item>', raw, re.S) or re.findall(r'<entry\b.*?</entry>', raw, re.S)
    for b in blocks:
        def g(tag):
            m = re.search(r'<%s[^>]*>(.*?)</%s>' % (tag, tag), b, re.S)
            if not m: return ''
            s = m.group(1)
            s = re.sub(r'<!\[CDATA\[(.*?)\]\]>', r'\1', s, flags=re.S)
            s = re.sub(r'<[^>]+>', ' ', s)
            s = s.replace('&#8217;', "'").replace('&#8216;', "'").replace('&#8220;', '"').replace('&#8221;', '"')
            s = s.replace('&#8230;', '...').replace('&#8211;', '-').replace('&amp;', '&').replace('&nbsp;', ' ')
            s = s.replace('&#039;', "'").replace('&quot;', '"').replace('&lt;', '<').replace('&gt;', '>')
            return re.sub(r'\s+', ' ', s).strip()
        title = g('title'); link = g('link') or g('guid')
        m = re.search(r'<link[^>]*href="([^"]+)"', b)
        if not link and m: link = m.group(1)
        pub = g('pubDate') or g('published') or g('updated') or g('dc:date')
        desc = g('description') or g('summary') or g('content:encoded')
        dt = None
        if pub:
            try:
                dt = email.utils.parsedate_to_datetime(pub)
                if dt.tzinfo is None: dt = dt.replace(tzinfo=datetime.timezone.utc)
            except Exception:
                try:
                    dt = datetime.datetime.fromisoformat(pub.replace('Z', '+00:00'))
                    if dt.tzinfo is None: dt = dt.replace(tzinfo=datetime.timezone.utc)
                except Exception:
                    dt = None
        out.append({'title': title, 'link': link, 'dt': dt, 'desc': desc[:400], 'raw_pub': pub})
    return out

for f in ['iaasia', 'ibm', 'scmp', 'govhk', 'artemis', 'ian_hk', 'ian_main']:
    p = os.path.join(D, f + '.out')
    if not os.path.exists(p):
        print('MISSING', f); continue
    items = parse_rss(p)
    fresh = [x for x in items if x['dt'] and hkt(x['dt']) > CUT]
    print('=====', f, 'total', len(items), 'fresh', len(fresh))
    for x in fresh[:25]:
        print(' *', hkt(x['dt']).strftime('%m-%d %H:%M'), '|', x['title'][:90])
        print('   ', x['link'][:130])
