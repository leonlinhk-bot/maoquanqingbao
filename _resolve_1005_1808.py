import re, html, glob, os, json, subprocess
CACHE = '/Users/leonliang/maoquanqingbao/data/_cache1005_1808/'
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/128 Safari/537.36'

WANT = {
    'gn_aia.txt': ['Z世代'],
    'gn_fam.txt': ['招商引資', '跨代財富傳承'],
    'gn_hkins2.txt': ['離岸人民幣創投'],
}

def resolve(gurl):
    try:
        out = subprocess.run(['curl', '-sL', '-m', '25', '--noproxy', '*', '-A', UA, gurl],
                             capture_output=True, text=True, timeout=40).stdout
    except Exception as e:
        return f'ERR {e}'
    m = re.search(r'data-n-au="([^"]+)"', out) or re.search(r'url=(https?%3A%2F%2F[^"&]+)', out)
    if m:
        return m.group(1)
    m = re.search(r'<a[^>]+href="(https?://(?!news\.google)[^"]+)"', out)
    if m:
        return m.group(1)
    return '(unresolved) ' + out[:200].replace('\n', ' ')

for f, keys in WANT.items():
    d = open(CACHE+f, encoding='utf-8', errors='replace').read()
    for b in re.findall(r'<item>(.*?)</item>', d, re.S):
        t = re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', b, re.S)
        title = t.group(1) if t else ''
        if any(k in title for k in keys):
            l = re.search(r'<link>(.*?)</link>', b, re.S)
            gurl = l.group(1) if l else ''
            print('TITLE:', html.unescape(title)[:100])
            print('  GN :', gurl[:120])
            print('  RES:', resolve(gurl)[:220])
            print()
