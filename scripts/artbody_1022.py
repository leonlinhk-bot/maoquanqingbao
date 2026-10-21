import re, html, json
from pathlib import Path
D = Path('/Users/leonliang/maoquanqingbao/data/_1022_0037')

def clean(t):
    t = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', t, flags=re.S)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = html.unescape(t)
    return re.sub(r'[ \t\xa0]+', ' ', t)

for name in ['art_chubb', 'art_marsh', 'art_acorn', 'art_easton']:
    p = D / f'body_{name}.html'
    txt = p.read_text(encoding='utf-8', errors='ignore')
    print(f'\n######## {name}')
    # try JSON-LD articleBody
    for m in re.finditer(r'"articleBody"\s*:\s*"(.*?)"\s*,\s*"', txt, re.S):
        body = m.group(1)
        body = body.encode().decode('unicode_escape', 'ignore')
        print('[JSONLD]', body[:2500])
        break
    else:
        # find the main article div
        m = re.search(r'<div class="entry-content[^"]*">(.*?)</div>\s*<div', txt, re.S)
        if m:
            body = clean(m.group(1))
            body = re.sub(r'\s+', ' ', body)
            print('[entry-content]', body[:2500])
        else:
            # fallback: paragraphs containing key words
            paras = re.findall(r'<p[^>]*>(.*?)</p>', txt, re.S)
            out = []
            for pp in paras:
                s = re.sub(r'\s+', ' ', clean(pp)).strip()
                if len(s) > 80:
                    out.append(s)
            print('[paras]', ' '.join(out[:8])[:2500])

print('\n\n===== IAN ian.json excerpts (skuld / cyclone) =====')
data = json.load(open(D / 'ian.json'))
for it in data:
    t = re.sub(r'<[^>]+>', '', it['title']['rendered'])
    if 'Skuld' in t or 'cyclone' in t.lower() or 'Sompo' in t:
        print('\n##', t, '|', it['date'], '|', it['link'])
        print('   ', re.sub(r'<[^>]+>', '', it['excerpt']['rendered']).strip()[:600])
