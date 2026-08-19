import re, html, os, json

FDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fetch')

# window.json links
w = json.load(open(os.path.join(FDIR, 'window.json')))
for key in ['g_insurtech', 'g_family', 'g_prudential', 'g_en_prudential']:
    for i in w.get(key, []):
        print(key, '|', i['pubDate'][:16], '|', i['title'][:60], '|', i['link'][:100])

print("\n--- bn_insurtech.html hrefs ---")
raw = open(os.path.join(FDIR, 'bn_insurtech.html'), encoding='utf-8', errors='replace').read()
cards = re.findall(r'<div class="news-card[^"]*"[^>]*>(.*?)(?=<div class="news-card|$)', raw, re.S)
for c in cards:
    t = re.search(r'class="title"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', c, re.S)
    if not t:
        continue
    title = html.unescape(re.sub(r'<[^>]+>', '', t.group(2))).strip()
    href = html.unescape(t.group(1))
    print('-', title[:70], '|', href[:130])
