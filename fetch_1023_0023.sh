#!/bin/bash
cd /Users/leonliang/maoquanqingbao
D=.cache1023_0023
mkdir -p $D
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"

fetch() {
  name=$1; url=$2
  code=$(curl -sL -m 30 -A "$UA" -H "Accept-Language: en,zh-HK;q=0.9" -o "$D/$name" -w "%{http_code}" "$url")
  sz=$(wc -c < "$D/$name" | tr -d ' ')
  echo "$name $code $sz"
}

fetch ian_hk.xml   "https://insuranceasianews.com/country/hong-kong/feed/" &
fetch ian_all.xml  "https://insuranceasianews.com/feed/" &
fetch rn.xml       "https://www.reinsurancene.ws/feed/" &
fetch ibm_asia.xml "https://www.insurancebusinessmag.com/asia/rss/" &
fetch iaasia.xml   "https://insuranceasia.com/rss.xml" &
fetch govhk.xml    "https://www.info.gov.hk/gia/rss/general_zh.xml" &
fetch artemis.xml  "https://www.artemis.bm/feed/" &
fetch scmp.xml     "https://www.scmp.com/rss/92/feed" &
fetch hkfi.html    "https://www.hkfi.org.hk/en/media-centre/press-release" &
fetch hkma.html    "https://www.hkma.gov.hk/eng/news-and-media/press-releases/" &
fetch hkma_rss.xml "https://www.hkma.gov.hk/eng/news-and-media/press-releases/rss/" &
fetch ia_press.html "https://www.ia.org.hk/en/infocenter/press_releases.html" &
fetch ia_circ.html "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html" &
fetch nfra.html    "https://www.nfra.gov.cn/cn/view/pages/index/index.html" &
fetch aia.html     "https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases/" &
fetch pru.html     "https://www.prudential.com.hk/tc/about-us/newsroom/" &
fetch axa.html     "https://www.axa.com.hk/zh/news-room/" &
fetch sunlife.html "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/" &
fetch manulife.html "https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html" &
wait
echo "=== done ==="
