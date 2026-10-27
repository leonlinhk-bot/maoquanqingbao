#!/usr/bin/env python3
"""Pull meta description / JSON-LD excerpt for the 3 chosen ian articles."""
import re, urllib.request, html, json

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0"}
urls = {
 "moodys": "https://insuranceasianews.com/apac-insurers-ability-to-reprice-risks-will-help-preserve-profitability-moodys/",
 "blackrock_captives": "https://insuranceasianews.com/onshore-captives-third-party-capital-primed-for-rapid-growth-in-apac-blackrock/",
 "cyber": "https://insuranceasianews.com/you-cant-fix-what-you-cant-see-cyber-insurers-warn-php2shell-website-shutdowns-highlight-ai-impact/",
}
for k, u in urls.items():
    h = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=35).read().decode('utf-8', 'ignore')
    print("\n###", k)
    for pat in [r'<meta name="description" content="(.*?)"', r'<meta property="og:description" content="(.*?)"']:
        m = re.search(pat, h, re.S)
        if m:
            print("DESC:", html.unescape(m.group(1))[:500])
    for m in re.finditer(r'"datePublished":"([^"]+)"|"dateModified":"([^"]+)"', h):
        print("DATE:", m.group(0))
    # JSON-LD articleBody if present
    for m in re.finditer(r'"articleBody":"(.{50,800}?)"', h):
        print("BODY:", m.group(1)[:600])
