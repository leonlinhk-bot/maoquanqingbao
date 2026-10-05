#!/usr/bin/env bash
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"
OUT=/Users/leonliang/maoquanqingbao/data/_cache1006_0049
gn() { # name query
  code=$(curl -sL -m 30 -A "$UA" -o "$OUT/$1" -w "%{http_code}" "https://news.google.com/rss/search?q=$2&hl=$3&gl=$4&ceid=$5")
  echo "$1 $code $(wc -c < "$OUT/$1" | tr -d ' ')"
}
gn gn_ia_site.xml  "site%3Aia.org.hk" "en-US" "US" "US%3Aen"
gn gn_hkma_site.xml "site%3Ahkma.gov.hk" "en-US" "US" "US%3Aen"
gn gn_baojianju.xml "%E4%BF%9D%E7%9B%A3%E5%B1%80" "zh-HK" "HK" "HK%3Azh-Hant"
gn gn_ia_zh.xml     "%E4%BF%9D%E9%9A%AA%E6%A5%AD%E7%9B%A3%E7%AE%A1%E5%B1%80" "zh-HK" "HK" "HK%3Azh-Hant"
gn gn_manulife_hk.xml "%E5%AE%8F%E5%88%A9+%E4%BF%9D%E9%9A%AA" "zh-HK" "HK" "HK%3Azh-Hant"
gn gn_hk_ins.xml    "%E9%A6%99%E6%B8%AF+%E4%BF%9D%E9%9A%AA+%E7%9B%A3%E7%AE%A1" "zh-HK" "HK" "HK%3Azh-Hant"
gn gn_hkfi.xml      "HKFI+OR+%22Hong+Kong+Federation+of+Insurance%22" "en-US" "US" "US%3Aen"
gn gn_iaa.xml       "insuranceasia" "en-US" "US" "US%3Aen"
echo DONE
