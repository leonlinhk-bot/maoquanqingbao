import re, html, os
CACHE = '/Users/leonliang/maoquanqingbao/data/_cache1006_0049/'


def cl(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()


KW = ['保險', '保監', '財經事務', '庫務', '積金', '強積金', '金管局', '金融', '施政報告', 'insur',
      'Insurance', 'Treasury', 'MPF', 'Financial Services', 'reinsurance', 'risk management']
for fn in ('govhk_zh.xml', 'govhk_en.xml'):
    data = open(CACHE + fn, encoding='utf-8', errors='ignore').read()
    print(f'===== {fn} =====')
    for m in re.finditer(r'<item>(.*?)</item>', data, re.S):
        b = m.group(1)
        t = re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', b, re.S)
        d = re.search(r'<pubDate>(.*?)</pubDate>', b, re.S)
        l = re.search(r'<link>(.*?)</link>', b, re.S)
        title = cl(t.group(1)) if t else ''
        if any(k in title for k in KW):
            print('  ', (d.group(1) if d else '?'), '|', title[:100])
            print('       ', (l.group(1) if l else ''))
