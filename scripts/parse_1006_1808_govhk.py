import re, html
RAW='/Users/leonliang/maoquanqingbao/data/_raw_1006_1808'
t=open(f'{RAW}/govhk_zh.xml',encoding='utf-8',errors='ignore').read()
ents=re.findall(r'<item[\s>].*?</item>', t, re.S)
print('total items', len(ents))
for e in ents:
    if '保監局（保險業監管局）會加強協調業界為貴金屬提供保險' in e or '黃金專線' in e:
        ti=re.search(r'<title><!\[CDATA\[(.*?)\]\]></title>', e, re.S)
        ln=re.search(r'<link>(.*?)</link>', e, re.S)
        d=re.search(r'<pubDate>(.*?)</pubDate>', e, re.S)
        print('HIT TITLE:', ti.group(1) if ti else '?')
        print('LINK:', ln.group(1) if ln else '?')
        print('DATE:', d.group(1) if d else '?')
        print('len', len(e))
print('---- items on 10-06 with 保險/金融 in description (short list) ----')
for e in ents:
    ti=re.search(r'<title><!\[CDATA\[(.*?)\]\]></title>', e, re.S)
    d=re.search(r'<pubDate>(.*?)</pubDate>', e, re.S)
    ln=re.search(r'<link>(.*?)</link>', e, re.S)
    body=re.sub(r'<[^>]+>',' ',e)
    if '06 Oct 2026' in (d.group(1) if d else '') and ('保險' in body):
        print('-', re.sub(r'\s+',' ',ti.group(1))[:80] if ti else '?', '|', ln.group(1) if ln else '', '|', d.group(1)[:25])
