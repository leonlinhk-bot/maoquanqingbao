#!/bin/bash
cd /Users/leonliang/maoquanqingbao
OUT=data/_raw_1007_1808
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
fetch() {
  curl -sSL --noproxy '*' --max-time 50 -A "$UA" "$2" -o "$OUT/$1" -w "%{http_code} %{size_download} $1\n" || echo "FAIL $1"
}
fetch ia_pr2.html "https://www.ia.org.hk/en/infocenter/press_releases/2026.html"
fetch ia_pr3.html "https://www.ia.org.hk/tc/infocenter/press_releases.html"
fetch artemis2.html "https://r.jina.ai/https://www.artemis.bm/news/"
fetch hkfi2.html "https://www.hkfi.org.hk/en/media-centre/press-releases"
fetch manulife2.html "https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html"
fetch ctf.html "https://www.ctflife.com.hk/tc/about-us/media-centre/press-releases.html"
fetch fwd.html "https://www.fwd.com.hk/en/about-fwd/media-centre/press-releases/"
fetch boclife.html "https://www.boclife.com.hk/tc/about-us/media-centre/press-releases.html"
fetch chinalife.html "https://www.chinalife.com.hk/tc/news"
fetch yflife.html "https://www.yflife.com/tc/media-centre/press-release.html"
fetch ia_stats.html "https://www.ia.org.hk/en/infocenter/statistics/statistics.html"
fetch sfc.html "https://apps.sfc.hk/edistributionWeb/gateway/TC/news-and-announcements/news/"
fetch hkma_fo.html "https://www.newcies.gov.hk/en/news-and-resources/news/"
echo DONE
