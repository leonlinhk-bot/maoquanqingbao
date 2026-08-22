#!/usr/bin/env python3
import re, html, glob, os

def parse_rss(path):
    txt = open(path, encoding='utf-8', errors='ignore').read()
    items = re.findall(r'<item>(.*?)</item>', txt, re.S)
    out = []
    for it in items:
        def g(tag):
            m = re.search(r'<%s[^>]*>(.*?)</%s>' % (tag, tag), it, re.S)
            return html.unescape(m.group(1)).strip() if m else ''
        out.append({'title': g('title'), 'link': g('link'), 'pubDate': g('pubDate')})
    return out

if __name__ == '__main__':
    for f in sorted(glob.glob('.tmp/0821b/m_*.html')):
        print('====', f, os.path.getsize(f), 'bytes')
        try:
            items = parse_rss(f)
            print('items:', len(items))
            for it in items[:25]:
                print(' -', it['pubDate'][:25], '|', it['title'][:80], '|', it['link'][:100])
        except Exception as e:
            print('ERR', e)
