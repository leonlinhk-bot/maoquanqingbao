#!/bin/bash
cd /Users/leonliang/maoquanqingbao
OUT=data/_raw_1007_1808
mkdir -p $OUT
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
fetch() { # name url
  curl -sSL --noproxy '*' --max-time 45 -A "$UA" "$2" -o "$OUT/$1" -w "%{http_code} %{size_download} $1\n" || echo "FAIL $1"
}
fetch ia_press.html "https://www.ia.org.hk/en/infocenter/press_releases.html"
fetch ia_circ.html "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html"
fetch ia_circ2.html "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters.html"
fetch hkma_press.html "https://www.hkma.gov.hk/eng/news-and-media/press-releases/"
fetch insuranceasia.rss "https://insuranceasia.com/rss.xml"
fetch ian.json "https://insuranceasianews.com/wp-json/wp/v2/posts?per_page=15"
fetch ibm_asia.html "https://www.insurancebusinessmag.com/asia/news/breaking-news/"
fetch scmp_ins.rss "https://www.scmp.com/rss/92/feed"
fetch hkfi.html "https://www.hkfi.org.hk/en/media-centre/press-release"
fetch artemis.html "https://www.artemis.bm/news/"
fetch nfra_list.html "https://www.nfra.gov.cn/cn/view/pages/index/index.html"
fetch govhk_zh.xml "https://www.info.gov.hk/gia/rss/general_zh.xml"
fetch aia.html "https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases/"
fetch manulife.html "https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html"
fetch prudential.html "https://www.prudential.com.hk/tc/about-us/newsroom/"
fetch axa.html "https://www.axa.com.hk/zh/news-room/"
fetch sunlife.html "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/"
fetch fstb.html "https://www.fstb.gov.hk/en/"
fetch mpfa.html "https://www.mpfa.org.hk/en/info-centre/press-releases"
fetch gnews_ia.xml "https://news.google.com/rss/search?q=%E4%BF%9D%E7%9B%A3%E5%B1%80+OR+%E4%BF%9D%E9%99%A9%E6%A5%AD%E7%9B%A3%E7%AE%A1%E5%B1%80&hl=zh-HK&gl=HK&ceid=HK:zh-Hant"
fetch gnews_ins.xml "https://news.google.com/rss/search?q=%E9%A6%99%E6%B8%AF+%E4%BF%9D%E9%9A%AA&hl=zh-HK&gl=HK&ceid=HK:zh-Hant"
fetch gnews_fo.xml "https://news.google.com/rss/search?q=%E5%AE%B6%E6%97%8F%E8%BE%A6%E5%85%AC%E5%AE%A4+OR+%E5%82%B3%E5%AE%B6%E8%BE%A6&hl=zh-HK&gl=HK&ceid=HK:zh-Hant"
fetch gnews_insurer.xml "https://news.google.com/rss/search?q=%E5%8F%8B%E9%82%A6+OR+%E4%BF%9D%E8%AA%A0+OR+%E5%AE%8F%E5%88%A9+OR+%E5%AE%89%E7%9B%9B+OR+%E6%B0%B8%E6%98%8E&hl=zh-HK&gl=HK&ceid=HK:zh-Hant"
fetch gnews_cn.xml "https://news.google.com/rss/search?q=%E4%BF%9D%E9%99%A9+%E7%9B%91%E7%AE%A1&hl=zh-CN&gl=CN&ceid=CN:zh-Hans"
fetch hkma_rss.xml "https://www.hkma.gov.hk/eng/rss/press-release.xml"
echo "DONE"
