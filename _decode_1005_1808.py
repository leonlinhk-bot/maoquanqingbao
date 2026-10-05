import base64, re, glob, os
CACHE = '/Users/leonliang/maoquanqingbao/data/_cache1005_1808/'

def decode(idb64):
    s = idb64.split('/')[-1].split('?')[0]
    s += '=' * (-len(s) % 4)
    try:
        raw = base64.urlsafe_b64decode(s)
    except Exception:
        return None
    # try utf-8 blocks
    for enc in ('utf-8', 'latin-1'):
        txt = raw.decode(enc, errors='ignore')
        m = re.findall(r'https?://[^\x00-\x20"\'\\]+', txt)
        if m:
            return m
    return None

WANT = {'gn_aia.txt': ['Z世代'], 'gn_fam.txt': ['招商引資', '跨代財富傳承', '離岸人民幣'],
        'gn_hkins2.txt': ['離岸人民幣'], 'gn_hk_ins.txt': ['跨代財富傳承', '醫療旅遊']}
for f, keys in WANT.items():
    d = open(CACHE+f, encoding='utf-8', errors='replace').read()
    for b in re.findall(r'<item>(.*?)</item>', d, re.S):
        t = re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', b, re.S)
        title = t.group(1) if t else ''
        if any(k in title for k in keys):
            l = re.search(r'<link>(.*?)</link>', b, re.S)
            gurl = (l.group(1) if l else '')
            print('TITLE:', title[:80])
            print('  DECODED:', (decode(gurl) if gurl else None))
