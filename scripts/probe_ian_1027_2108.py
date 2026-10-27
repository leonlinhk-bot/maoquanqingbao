#!/usr/bin/env python3
"""InsuranceAsia News WP posts + dedupe against live-items."""
import json, urllib.request

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"}
url = "https://insuranceasianews.com/wp-json/wp/v2/posts?per_page=15&_fields=id,date,modified,link,title"
req = urllib.request.Request(url, headers=UA)
posts = json.loads(urllib.request.urlopen(req, timeout=30).read().decode())

d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
items = d['items'] if isinstance(d, dict) else d
known = {i.get('originalUrl', '').rstrip('/') for i in items}
known_slug = {i['id'] for i in items}

print("server time:", __import__('datetime').datetime.now().isoformat())
for p in posts:
    title = p['title']['rendered'].replace('&#8217;', "'").replace('&amp;', '&')
    link = p['link']
    new = link.rstrip('/') not in known
    print(f"{p['date']} | new={new} | {title[:80]} | {link}")
