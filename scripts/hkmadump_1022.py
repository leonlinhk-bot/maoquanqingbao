import re, html
D = '/Users/leonliang/maoquanqingbao/data/_1022_0037'
txt = open(D + '/hkma.html', encoding='utf-8', errors='ignore').read()
i = txt.find('20261021')
print(txt[max(0, i-3000):i+3000])
