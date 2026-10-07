#!/bin/bash
cd /Users/leonliang/maoquanqingbao
OUT=data/_raw_1006_1808
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
jf() { # name url
  curl -s --noproxy '*' --max-time 60 -A "$UA" "https://r.jina.ai/$2" -o "$OUT/$1" -w "%{http_code} %{size_download} $1\n" || echo "FAIL $1"
}
fetch() {
  curl -sSL --noproxy '*' --max-time 45 -A "$UA" "$2" -o "$OUT/$1" -w "%{http_code} %{size_download} $1\n" || echo "FAIL $1"
}
# MPFA press releases (積金局)
fetch mpfa.html "https://www.mpfa.org.hk/en/info-centre/press-releases"
fetch mpfa_zh.html "https://www.mpfa.org.hk/tc/info-centre/press-releases"
# NFRA
fetch nfra_news2.html "https://www.nfra.gov.cn/cn/view/pages/ItemList.html?itemPId=923&itemId=915&itemUrl=ItemListRightList.html&itemName=%E7%9B%91%E7%AE%A1%E5%8A%A8%E6%80%81"
# jina for JS-heavy / blocked pages
jf j_manulife.txt "https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html"
jf j_pru.txt "https://www.prudential.com.hk/tc/about-us/newsroom/"
jf j_aia.txt "https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases/"
jf j_artemis.txt "https://www.artemis.bm/news/"
jf j_ia_press.txt "https://www.ia.org.hk/en/infocenter/press_releases.html"
jf j_sunlife.txt "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/"
echo DONE
