import re, os, datetime, email.utils
D = 'data/_raw_1010_0110'
h = open(os.path.join(D, 'govhk.out'), encoding='utf-8', errors='replace').read()
blocks = re.findall(r'<item\b.*?</item>', h, re.S)
KW = ['保險', '保監', '強積金', '積金', '年金', '醫療', '醫保', '理賠', '再保險', '專屬自保', '金管局', '財經事務', '金融', '退休', '財富', '銀行', '投資', '上市公司', '保險業']
out = []
for b in blocks:
    def g(tag):
        m = re.search(r'<%s[^>]*>(.*?)</%s>' % (tag, tag), b, re.S)
        if not m: return ''
        s = re.sub(r'<!\[CDATA\[(.*?)\]\]>', r'\1', m.group(1), flags=re.S)
        return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', s)).strip()
    t = g('title'); link = g('link') or g('guid'); pub = g('pubDate')
    if not t: continue
    try:
        dt = email.utils.parsedate_to_datetime(pub)
    except Exception:
        dt = None
    dstr = dt.strftime('%m-%d %H:%M') if dt else '?'
    if dt and dt.strftime('%Y-%m-%d') >= '2026-10-09' and any(k in t for k in KW):
        out.append((dstr, t, link))
print('govhk relevant fresh:', len(out))
for d, t, l in out:
    print(' *', d, '|', t[:95])
    print('   ', l)
