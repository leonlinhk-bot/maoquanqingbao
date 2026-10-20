import re, html, sys, glob

for p in sorted(glob.glob('data/_1021_1808/bodies/*.html')):
    raw = open(p, encoding='utf-8', errors='replace').read()
    raw = re.sub(r'<script.*?</script>', ' ', raw, flags=re.S)
    raw = re.sub(r'<style.*?</style>', ' ', raw, flags=re.S)
    paras = re.findall(r'<p[^>]*>(.*?)</p>', raw, re.S)
    out = []
    for x in paras:
        t = re.sub(r'<[^>]+>', ' ', x)
        t = re.sub(r'\s+', ' ', html.unescape(t)).strip()
        if len(t) > 60:
            out.append(t)
    name = p.split('/')[-1].replace('.html', '')
    print(f'\n######## {name}  ({len(out)} paras)')
    print('\n'.join(out[:10])[:2600])
