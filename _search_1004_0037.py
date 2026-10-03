import urllib.request, urllib.parse, re, html, json, datetime

UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36'

queries = [
    '香港保险业监管局 通函 2026年10月',
    'Hong Kong Insurance Authority circular October 2026',
    'HKMA press release October 2026 insurance',
    'insurance news Hong Kong October 3 2026',
]

def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept': 'text/html'})
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.read().decode('utf-8', 'ignore')

def clean(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()

for q in queries:
    print('=' * 70)
    print('Q:', q)
    for base in ['https://html.duckduckgo.com/html/?q=', 'https://lite.duckduckgo.com/lite/?q=']:
        try:
            t = fetch(base + urllib.parse.quote(q))
            links = re.findall(r'<a[^>]+class="result__a"[^>]*>(.*?)</a>', t, re.S)[:6]
            if not links:
                links = re.findall(r'<a[^>]+href="(http[^"]+)"[^>]*>(.*?)</a>', t, re.S)[:6]
            for l in links:
                print('  -', clean(l if isinstance(l, str) else l[1])[:120] if isinstance(l, str) else clean(l[1])[:120])
            if links:
                break
        except Exception as e:
            print('  err', base, str(e)[:80])
