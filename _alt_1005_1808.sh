#!/usr/bin/env bash
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/128 Safari/537.36"
OUT=/Users/leonliang/maoquanqingbao/data/_cache1005_1808
echo "--- noproxy direct ---"
curl -sL -m 25 --noproxy '*' -A "$UA" -o "$OUT/np_ia.html" -w "ia_noproxy %{http_code} %{size_download}\n" "https://www.ia.org.hk/en/infocenter/press_releases.html"
curl -sL -m 25 --noproxy '*' -A "$UA" -o "$OUT/np_manu.html" -w "manu_noproxy %{http_code} %{size_download}\n" "https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html"
echo "--- bing search IA ---"
curl -sL -m 30 -A "$UA" --get "https://www.bing.com/search" --data-urlencode "q=site:ia.org.hk press release" --data-urlencode "mkt=zh-HK" -o "$OUT/bing_ia.html" -w "bing %{http_code} %{size_download}\n"
echo "--- duckduckgo html ---"
curl -sL -m 30 -A "$UA" --get "https://html.duckduckgo.com/html/" --data-urlencode "q=site:ia.org.hk 保監局" -o "$OUT/ddg_ia.html" -w "ddg %{http_code} %{size_download}\n"
echo DONE
