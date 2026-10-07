import re, os, html, json
RAW = '/Users/leonliang/maoquanqingbao/data/_raw_1007_1808'
for f in ['art_pru_japan.html','art_asic.html','art_india_div.html','art_iag.html']:
    t = open(os.path.join(RAW,f), encoding='utf-8', errors='ignore').read()
    print('#'*20, f)
    for pat in [r'"datePublished"\s*:\s*"([^"]+)"', r'article:published_time"\s+content="([^"]+)"', r'"date_gmt"\s*:\s*"([^"]+)"', r'"date"\s*:\s*"([^"]+)"']:
        m = re.search(pat, t)
        print('   ', pat[:28], '=>', m.group(1) if m else None)
    # lede
    m = re.search(r'property="og:description" content="([^"]{20,600})"', t)
    print('    og:desc:', html.unescape(m.group(1))[:400] if m else None)
