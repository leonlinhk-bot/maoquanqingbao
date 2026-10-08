#!/bin/bash
cd /Users/leonliang/maoquanqingbao || exit 1
D=data/_jina_1009_0027
mkdir -p "$D"
curl -s --max-time 50 -A "Mozilla/5.0" "https://r.jina.ai/https://www.ia.org.hk/en/infocenter/press_releases.html" -o "$D/ia_press.txt"
echo "ia_press $(wc -c < "$D/ia_press.txt" | tr -d ' ')"
curl -s --max-time 50 -A "Mozilla/5.0" "https://r.jina.ai/https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html" -o "$D/manulife.txt"
echo "manulife $(wc -c < "$D/manulife.txt" | tr -d ' ')"
curl -s --max-time 50 -A "Mozilla/5.0" "https://r.jina.ai/https://www.prudential.com.hk/tc/about-us/newsroom/" -o "$D/prudential.txt"
echo "prudential $(wc -c < "$D/prudential.txt" | tr -d ' ')"
curl -s --max-time 50 -A "Mozilla/5.0" "https://r.jina.ai/https://www.axa.com.hk/zh/news-room/" -o "$D/axa.txt"
echo "axa $(wc -c < "$D/axa.txt" | tr -d ' ')"
curl -s --max-time 50 -A "Mozilla/5.0" "https://r.jina.ai/https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/" -o "$D/sunlife.txt"
echo "sunlife $(wc -c < "$D/sunlife.txt" | tr -d ' ')"
curl -s --max-time 50 -A "Mozilla/5.0" "https://r.jina.ai/https://www.hkfi.org.hk/media-release" -o "$D/hkfi.txt"
echo "hkfi $(wc -c < "$D/hkfi.txt" | tr -d ' ')"
