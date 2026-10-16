import re, html
from datetime import datetime, timezone, timedelta
HK = timezone(timedelta(hours=8))
D = '/Users/leonliang/maoquanqingbao/data/_1016_1808/'
for f in ['aia.out', 'prudential.out', 'axa.out', 'sunlife.out']:
    raw = open(D + f, encoding='utf-8', errors='replace').read()
    txt = re.sub(r'<script.*?</script>', ' ', raw, flags=re.S)
    txt = re.sub(r'<[^>]+>', ' ', txt)
    txt = html.unescape(txt)
    txt = re.sub(r'\s+', ' ', txt)
    print('=====', f, 'len', len(txt))
    # find date-like tokens
    ds = sorted(set(re.findall(r'20\d{2}[-/年]\s?\d{1,2}[-/月]\s?\d{1,2}', txt)))
    print('dates:', ds[-14:])
    # print a window around 2026-10-1x mentions
    for m in re.finditer(r'2026\s?[-/年]\s?10\s?[-/月]\s?1[0-9]', txt):
        print('   ...', txt[max(0, m.start()-90):m.start()+70].strip()[:170])
