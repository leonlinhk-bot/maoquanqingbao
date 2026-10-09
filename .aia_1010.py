import re, os, json
D = 'data/_raw_1010_0110'
a = open(os.path.join(D, 'aia2026.out'), encoding='utf-8', errors='replace').read()
cards = re.findall(r'<a class="cmp-promotioncard__link" href="([^"]+)">\s*<div class="cmp-promotioncard__content">\s*<div class="cmp-promotioncard__title cmp-promotioncard__hk-title">\s*(.*?)\s*</div>\s*<div class="cmp-promotioncard__text">\s*<div class="cmp-promotioncard__date">\s*(.*?)\s*</div>', a, re.S)
print('AIA cards:', len(cards))
for u, t, d in cards[:14]:
    print(' *', d, '|', t[:80], '|', u[:100])
if not cards:
    cards2 = re.findall(r'class="cmp-promotioncard__link" href="([^"]+)"', a)
    print('fallback links:', len(cards2), cards2[:8])
    for m in list(re.finditer(r'cmp-promotioncard__hk-title">(.{0,120}?)</div>', a))[:14]:
        print('  T:', re.sub(r'\s+', ' ', m.group(1))[:90])
    for m in list(re.finditer(r'class="cmp-promotioncard__date">\s*(.{0,40}?)\s*</div>', a))[:14]:
        print('  D:', re.sub(r'\s+', ' ', m.group(1)))
