import re, html
from pathlib import Path
D = Path('/Users/leonliang/maoquanqingbao/data/_1022_0037')
txt = (D / 'hkfi.html').read_text(encoding='utf-8', errors='ignore')
for m in re.finditer(r'2026-10-(19|20|21|22)', txt):
    s = max(0, m.start() - 700)
    seg = txt[s:m.end() + 300]
    seg = re.sub(r'<script.*?</script>', ' ', seg, flags=re.S)
    seg = html.unescape(re.sub(r'<[^>]+>', ' ', seg))
    seg = re.sub(r'\s+', ' ', seg).strip()
    print('>>>', seg[-450:])
    print('-' * 60)

print('\n\n===== SUN LIFE date scan =====')
txt2 = (D / 'sun.html').read_text(encoding='utf-8', errors='ignore')
# sunlife releases 2026 - look for titles + any yyyy年m月d日
for m in re.finditer(r'(20\d\d)年(\d{1,2})月(\d{1,2})日', txt2):
    print(m.group(0), end=' | ')
print()
