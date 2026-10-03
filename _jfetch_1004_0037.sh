#!/bin/bash
cd /Users/leonliang/maoquanqingbao
D=data/_jina_1004_0037
mkdir -p "$D"
jfetch() {
  local url="$1" out="$2"
  curl -s --max-time 60 "https://r.jina.ai/$url" -o "$D/$out"
  echo "$out $(wc -c < "$D/$out" | tr -d ' ')"
}
jfetch "https://www.ia.org.hk/en/infocenter/press_releases.html" ia_press.txt
jfetch "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html" ia_circ.txt
jfetch "https://www.hkma.gov.hk/eng/news-and-media/press-releases/" hkma.txt
jfetch "https://www.insurancebusinessmag.com/asia/news/breaking-news/" ibm_asia.txt
jfetch "https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases/" aia.txt
jfetch "https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html" manu.txt
jfetch "https://www.nfra.gov.cn/cn/view/pages/ItemList.html?itemPId=923&itemId=931&itemUrl=ItemListRightList.html&itemName=%E7%9B%91%E7%AE%A1%E5%8A%A8%E6%80%81" nfra.txt
