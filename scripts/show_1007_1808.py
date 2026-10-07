import re, os, html, sys
RAW = '/Users/leonliang/maoquanqingbao/data/_raw_1007_1808'
def txt(f, n=2600):
    t = open(os.path.join(RAW, f), encoding='utf-8', errors='ignore').read()
    t = re.sub(r'<script.*?</script>', ' ', t, flags=re.S)
    t = re.sub(r'<style.*?</style>', ' ', t, flags=re.S)
    t = re.sub(r'<nav.*?</nav>', ' ', t, flags=re.S)
    t = re.sub(r'<header.*?</header>', ' ', t, flags=re.S)
    t = re.sub(r'<footer.*?</footer>', ' ', t, flags=re.S)
    t = re.sub(r'<(br|/p|/div|/h\d)>', '\n', t)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = html.unescape(t)
    t = re.sub(r'[ \t]+', ' ', t)
    lines = [l.strip() for l in t.split('\n') if len(l.strip()) > 40]
    # dedupe consecutive
    out = []
    for l in lines:
        if not out or l != out[-1]:
            out.append(l)
    return '\n'.join(out)[:n]

files = sys.argv[1:]
for f in files:
    print('#'*35, f)
    print(txt(f))
    print()
