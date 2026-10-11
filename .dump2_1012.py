import re, html, sys
D='.tmp/1012_0022'
def totext(s):
    s=re.sub(r'<script.*?</script>','',s,flags=re.S)
    s=re.sub(r'<style.*?</style>','',s,flags=re.S)
    s=re.sub(r'<[^>]+>',' | ',s)
    s=html.unescape(s)
    s=re.sub(r'(\s*\|\s*)+',' | ',s)
    return re.sub(r'[ \t]+',' ',s)
for f in sys.argv[1:]:
    t=open(f'{D}/{f}',encoding='utf-8',errors='ignore').read()
    x=totext(t)
    print('#'*30, f, len(x))
    print(x[:2600])
    print('...')
