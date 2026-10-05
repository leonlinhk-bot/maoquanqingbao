#!/usr/bin/env bash
# Probe alternatives for IA / Manulife / HKFI
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"
OUT=/Users/leonliang/maoquanqingbao/data/_cache1005_1808
t() { echo -n "$1 -> "; curl -sL -m 25 -A "$UA" "$2" -o "$OUT/p_$1" -w "%{http_code} %{size_download}\n"; }

# IA press release RSS (IA publishes an RSS)
t ia_rss1 "https://www.ia.org.hk/en/infocenter/press_releases.rss"
t ia_rss2 "https://www.ia.org.hk/en/infocenter/rss/press_releases.xml"
# sitemap route
t ia_sitemap "https://www.ia.org.hk/sitemap.xml"
# with referer + accept
echo -n "ia_with_ref -> "
curl -sL -m 25 -A "$UA" -H "Referer: https://www.google.com/" -H "Accept: text/html,application/xhtml+xml" -H "Accept-Language: en-US,en;q=0.9" "https://www.ia.org.hk/en/infocenter/press_releases.html" -o "$OUT/p_ia_ref" -w "%{http_code} %{size_download}\n"
echo -n "manulife_ref -> "
curl -sL -m 25 -A "$UA" -H "Referer: https://www.google.com/" -H "Accept-Language: zh-HK,zh;q=0.9" "https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html" -o "$OUT/p_manu_ref" -w "%{http_code} %{size_download}\n"
echo -n "hkfi2 -> "
curl -sL -m 25 -A "$UA" "https://www.hkfi.org.hk/en/media-centre/press-release" -o "$OUT/p_hkfi2" -w "%{http_code} %{size_download}\n"
echo -n "nfra_stats -> "
curl -sL -m 25 -A "$UA" "https://www.nfra.gov.cn/cn/view/pages/ItemList.html?itemPId=923&itemId=931&itemUrl=ItemListRightList.html" -o "$OUT/p_nfra_stats" -w "%{http_code} %{size_download}\n"
echo DONE
