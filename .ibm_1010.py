import re, os
files = {
 'driver-assist': '/Users/leonliang/.hermes/cache/web/www.insurancebusinessmag.com-f647b39818.md',
 'thailand-disaster': '/Users/leonliang/.hermes/cache/web/www.insurancebusinessmag.com-b304aa15e2.md',
 'insurance-moves': '/Users/leonliang/.hermes/cache/web/www.insurancebusinessmag.com-51110a875f.md',
 'singapore-ai': '/Users/leonliang/.hermes/cache/web/www.insurancebusinessmag.com-ee87203457.md',
}
for k, p in files.items():
    if not os.path.exists(p):
        print('MISSING', k, p); continue
    t = open(p, encoding='utf-8', errors='replace').read()
    # drop nav-ish lines
    lines = [l for l in t.split('\n') if not re.match(r'^\s*[-*]\s*\[', l)]
    body = '\n'.join(lines)
    # find start after "SIGN UP" or after the last '- [News]'
    idx = body.find('Resources')
    print('#####', k, 'len', len(body))
    print(re.sub(r'\n{2,}', '\n', body[2000:6500]))
    print('\n\n')
