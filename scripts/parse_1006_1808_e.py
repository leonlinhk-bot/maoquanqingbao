import re, html
RAW='/Users/leonliang/maoquanqingbao/data/_raw_1006_1808'
def p(s): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',s))).strip()
t=open(f'{RAW}/mpfa.html',encoding='utf-8',errors='ignore').read()
print('=== MPFA press releases ===')
for m in re.finditer(r'(20\d\d[-/年]\s?\d{1,2}[-/月]\s?\d{1,2})', t):
    seg=p(t[m.start():m.start()+220])
    print('-', seg[:180])
    if m.start() > 40000: break
print('\n=== MPFA zh ===')
t2=open(f'{RAW}/mpfa_zh.html',encoding='utf-8',errors='ignore').read()
for m in re.finditer(r'(20\d\d年\d{1,2}月\d{1,2}日)', t2):
    seg=p(t2[max(0,m.start()-120):m.start()+180])
    print('-', seg[:200])
print('\n=== IA press html raw hints ===')
t3=open(f'{RAW}/ia_press.html',encoding='utf-8',errors='ignore').read()
print(t3[:1500])
print('\n=== NFRA news2 ===')
print(p(open(f'{RAW}/nfra_news2.html',encoding='utf-8',errors='ignore').read())[:600])
