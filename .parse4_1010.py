import re, os
D = 'data/_raw_1010_0110'
a = open(os.path.join(D, 'aia2026.out'), encoding='utf-8', errors='replace').read()
print('--- aia: press release links ---')
for m in list(re.finditer(r'media-centre/press-releases/2026[^"&#]*', a))[:0]:
    pass
idx = [m.start() for m in re.finditer(r'press-releases', a)]
print('occurrences:', len(idx))
for i in idx[-6:]:
    print('...', re.sub(r'\s+', ' ', a[max(0, i - 500):i + 500])[:900])
    print('---')
print('--- aia: date strings ---')
for m in list(re.finditer(r'(2026[年/-]\s*1?0[月/-]\s*\d{1,2}|\d{1,2}\s+Oct(ober)?\s+2026)', a))[:10]:
    print(m.group(1), '||', re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', a[max(0, m.start() - 300):m.start() + 300]))[:250])
    print('---')

p = open(os.path.join(D, 'prudential.out'), encoding='utf-8', errors='replace').read()
print('--- prudential: dates ---')
for m in list(re.finditer(r'"(date|publishedDate|datePublished|lastModified)"\s*:\s*"([^"]{6,30})"', p))[:12]:
    print(m.group(1), m.group(2))
print('--- prudential: title-ish links ---')
for m in list(re.finditer(r'(newsroom/[^"\']{3,120})', p))[:12]:
    print(m.group(1))
