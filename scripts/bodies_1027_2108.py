#!/usr/bin/env python3
"""Fetch bodies of candidate insuranceasianews articles."""
import re, urllib.request, html

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0"}
urls = [
 "https://insuranceasianews.com/apac-insurers-ability-to-reprice-risks-will-help-preserve-profitability-moodys/",
 "https://insuranceasianews.com/onshore-captives-third-party-capital-primed-for-rapid-growth-in-apac-blackrock/",
 "https://insuranceasianews.com/blackrock-rethink-the-rules-how-taa-and-etfs-are-reshaping-portfolio-construction/",
 "https://insuranceasianews.com/you-cant-fix-what-you-cant-see-cyber-insurers-warn-php2shell-website-shutdowns-highlight-ai-impact/",
 "https://insuranceasianews.com/apac-offers-growth-diversification-for-global-reinsurers-gallagher-re/",
]

def strip(t):
    t = re.sub(r'<script.*?</script>', ' ', t, flags=re.S)
    t = re.sub(r'<style.*?</style>', ' ', t, flags=re.S)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = html.unescape(t)
    return re.sub(r'\s+', ' ', t).strip()

for u in urls:
    print("\n" + "=" * 70)
    print(u)
    try:
        req = urllib.request.Request(u, headers=UA)
        h = urllib.request.urlopen(req, timeout=35).read().decode('utf-8', 'ignore')
        t = re.search(r'<title>(.*?)</title>', h, re.S)
        print("TITLE:", strip(t.group(1)) if t else "?")
        m = re.search(r'<time[^>]*datetime="([^"]+)"', h)
        print("TIME:", m.group(1) if m else "?")
        art = re.search(r'<article.*?</article>', h, re.S) or re.search(r'class="[^"]*entry-content[^"]*"(.*?)</div>\s*</div>', h, re.S)
        body = strip(art.group(0)) if art else ""
        if len(body) < 300:
            body = strip(h)
        print("BODY:", body[:2200])
    except Exception as e:
        print("ERR", type(e).__name__, e)
