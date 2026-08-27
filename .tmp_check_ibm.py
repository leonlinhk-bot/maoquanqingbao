import re, urllib.request, json

arts = [
    'hdi-global-targets-lead-market-position-in-fine-art-and-specie-587369',
    'rogue-ai-breach-exposes-cyber-coverage-gap-for-brokers-587236',
    'indonesias-assetseizure-risk-lacks-the-cover-haze-already-has-587238',
    'mas-confirms-old-critical-illness-policies-wont-get-updated-definitions-587235',
    'wtw-flags-structural-shift-beneath-general-aviation-insurance-soft-market-587179',
]
for slug in arts:
    url = f'https://www.insurancebusinessmag.com/asia/news/{slug}.aspx'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36'})
        html = urllib.request.urlopen(req, timeout=30).read().decode('utf-8', 'ignore')
        title = re.search(r'<title>(.*?)</title>', html, re.S)
        # look for datePublished / datetime
        dp = re.findall(r'"datePublished"\s*:\s*"([^"]+)"', html)
        dt = re.findall(r'datetime="([^"]+)"', html)
        tm = re.findall(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2})', html)
        print(slug[:50], '| datePublished:', dp[:1], '| datetime:', dt[:2], '| tm:', tm[:2], '|', (title.group(1).strip()[:70] if title else '?'))
    except Exception as e:
        print(slug, 'ERR', e)
