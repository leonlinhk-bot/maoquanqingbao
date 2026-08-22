import re, html, glob

def get_date(raw):
    for p in [r'property="article:published_time"\s+content="([^"]+)"',
              r'"datePublished"\s*:\s*"([^"]+)"',
              r'name="date"\s+content="([^"]+)"',
              r'(\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+20\d{2})',
              r'(20\d{2}-\d{1,2}-\d{1,2})']:
        m = re.search(p, raw)
        if m:
            return m.group(1)
    return ''

def get_body(raw):
    body = re.sub(r'<script.*?</script>', ' ', raw, flags=re.S)
    body = re.sub(r'<style.*?</style>', ' ', body, flags=re.S)
    body = re.sub(r'<[^>]+>', ' ', body)
    body = html.unescape(re.sub(r'\s+', ' ', body))
    return body

for f in sorted(glob.glob('.tmp/0821/air_*.html')):
    raw = open(f, encoding='utf-8', errors='ignore').read()
    m = re.search(r'<title>(.*?)</title>', raw, re.S)
    t = html.unescape(m.group(1)).strip() if m else ''
    d = get_date(raw)
    body = get_body(raw)
    # find meaningful text window
    i = body.find('2026')
    print('=' * 80)
    print(f'{f.split("/")[-1]} | DATE: {d}')
    print(f'TITLE: {t[:130]}')
    # print first ~900 chars around main content
    j = body.find('More from')
    seg = body[200:2000]
    print('BODY:', seg[:900])
