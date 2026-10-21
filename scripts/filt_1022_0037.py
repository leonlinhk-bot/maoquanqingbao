import json, datetime, re
p = '/Users/leonliang/maoquanqingbao/data/_1022_0037/window.json'
items = json.load(open(p))
KW = ['insur', '保監', '保险', '保險', 'reinsur', '再保', 'annuit', '年金', 'underwrit', '承保', 'actuar',
      'policyholder', '保單', 'policy ', 'claims', '理賠', '索償', 'cat bond', '巨災', 'catastroph',
      'family office', '家辦', '家族辦公室', 'MPF', '強積金', '强积金', 'wealth', '財富', 'high-net',
      'regulat', '監管', '监管', 'HKMA', '金管局', 'IA ', 'Insurance Authority', 'solvency', '償付',
      'cyber', '網絡風險', 'mutual', 'takaful', 'broker', '經紀', 'agent', '代理人', 'health', '醫保', '医疗']
def hit(t):
    low = t.lower()
    return [k for k in KW if k.lower() in low]

rows = []
for it in items:
    keys = hit(it['title'] + ' ' + (it.get('desc') or ''))
    if keys:
        rows.append((it['dt'], it['src'], it['title'], keys[:4], it['link'], it.get('desc', '')[:120]))

rows.sort(reverse=True)
print('filtered:', len(rows), '/ total window:', len(items))
for dt, src, title, keys, link, desc in rows:
    print(f"\n{dt[5:16]} | {src} | {title}")
    print(f"   keys={keys}")
    print(f"   {link}")
    if desc:
        print(f"   {desc}")
