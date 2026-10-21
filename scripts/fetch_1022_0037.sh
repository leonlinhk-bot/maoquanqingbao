#!/usr/bin/env bash
# 2026-10-22 00:37 collection: raw pulls
cd /Users/leonliang/maoquanqingbao
D=data/_1022_0037
mkdir -p $D
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36'

fetch() { # url outfile
  code=$(curl -sL -m 25 -A "$UA" -o "$2" -w '%{http_code}' "$1" 2>/dev/null)
  echo "$code  $2  $(wc -c < "$2" | tr -d ' ')"
}

fetch 'https://artemis.bm/feed/'                                    $D/artemis.xml
fetch 'https://insuranceasianews.com/wp-json/wp/v2/posts?per_page=20&_fields=id,date,link,title,excerpt' $D/ian.json
fetch 'https://api.hkma.gov.hk/public/press-releases?lang=en&offset=0' $D/hkma_api.json
fetch 'https://www.insurancebusinessmag.com/asia/rss/'              $D/ibm_rss.xml
fetch 'https://www.reinsurancene.ws/feed/'                          $D/reins.xml
fetch 'https://www.info.gov.hk/gia/rss/general_zh.xml'              $D/govhk.xml
fetch 'https://www.scmp.com/rss/92/feed'                            $D/scmp.xml
fetch 'https://insuranceasia.com/insurance/rss.xml'                 $D/iaasia.xml
fetch 'https://www.ia.org.hk/en/infocenter/press_releases.html'     $D/ia_press.html
fetch 'https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html' $D/ia_circ.html
fetch 'https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases/' $D/aia.html
fetch 'https://www.prudential.com.hk/tc/about-us/newsroom/'         $D/pru.html
fetch 'https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html' $D/manu.html
fetch 'https://www.axa.com.hk/zh/news-room/'                        $D/axa.html
fetch 'https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/' $D/sun.html
fetch 'https://www.hkfi.org.hk/en/media-centre/press-release'       $D/hkfi.html
fetch 'https://www.nfra.gov.cn/cn/view/pages/index/index.html'      $D/nfra.html
