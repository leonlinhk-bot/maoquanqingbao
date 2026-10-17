#!/usr/bin/env bash
mkdir -p .cache1017_1836
cd .cache1017_1836
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
fetch() {
  code=$(curl -sL -m 45 -A "$UA" -o "$1" -w "%{http_code}" "$2" 2>/dev/null)
  echo "$1 $code $(wc -c < "$1" | tr -d ' ')"
}
fetch ia_press.html "https://www.ia.org.hk/en/infocenter/press_releases.html" &
fetch ia_circ.html "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html" &
fetch hkma.html "https://www.hkma.gov.hk/eng/news-and-media/press-releases/" &
fetch insuranceasia.xml "https://insuranceasia.com/rss.xml" &
fetch ibm_rss.xml "https://www.insurancebusinessmag.com/asia/rss/" &
fetch ian.json "https://insuranceasianews.com/wp-json/wp/v2/posts?per_page=20" &
fetch artemis.xml "https://www.artemis.bm/news/feed/" &
fetch rn.xml "https://www.reinsurancene.ws/feed/" &
wait
fetch aia.html "https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases/" &
fetch manulife.html "https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html" &
fetch prudential.html "https://www.prudential.com.hk/tc/about-us/newsroom/" &
fetch axa.html "https://www.axa.com.hk/zh/news-room/" &
fetch sunlife.html "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/" &
fetch hkfi.html "https://www.hkfi.org.hk/en/media-centre/press-release" &
fetch govhk.xml "https://www.info.gov.hk/gia/rss/general_zh.xml" &
fetch iaasia.html "https://www.asiainsurancereview.com/News/Latest-News?page=1" &
wait
echo done
