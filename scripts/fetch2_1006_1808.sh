#!/bin/bash
cd /Users/leonliang/maoquanqingbao
OUT=data/_raw_1006_1808
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
fetch() {
  curl -sSL --noproxy '*' --max-time 45 -A "$UA" "$2" -o "$OUT/$1" -w "%{http_code} %{size_download} $1\n" || echo "FAIL $1"
}
fetch hkma1006_4.html "https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/10/20261006-4/"
fetch hkma1006_3.html "https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/10/20261006-3/"
fetch ibm_hdi.html "https://www.insurancebusinessmag.com/asia/news/professional-liability/hdi-global-expands-medical-malpractice-into-global-healthcare-unit-592443.aspx"
fetch aia.html "https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases/"
fetch manulife.html "https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html"
fetch prudential.html "https://www.prudential.com.hk/tc/about-us/newsroom/"
fetch axa.html "https://www.axa.com.hk/zh/news-room/"
fetch sunlife.html "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/"
fetch ia_news.html "https://www.ia.org.hk/en/infocenter/press_releases.html"
fetch fstb.html "https://www.fstb.gov.hk/en/"
fetch scmp_insurance.html "https://www.scmp.com/topics/insurance"
fetch hkfi2.html "https://www.hkfi.org.hk/en/media-centre/press-release/"
fetch ia_stats.html "https://www.ia.org.hk/en/infocenter/statistics/statistics.html"
echo "DONE"
