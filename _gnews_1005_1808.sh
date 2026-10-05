#!/usr/bin/env bash
# 1005 18:08 Google News RSS sweep (search fallback for bot-blocked sources)
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/128 Safari/537.36"
OUT=/Users/leonliang/maoquanqingbao/data/_cache1005_1808
g() {
  local q="$1" out="$2"
  curl -s --max-time 30 -A "$UA" --get "https://news.google.com/rss/search" \
    --data-urlencode "q=$q" --data-urlencode "hl=zh-HK" --data-urlencode "gl=HK" --data-urlencode "ceid=HK:zh-Hant" \
    -o "$OUT/$out"
  echo "$out $(wc -c < "$OUT/$out" | tr -d ' ')"
}
g "保險業監管局 when:2d" gn_ia_zh.txt
g "\"Insurance Authority\" Hong Kong when:2d" gn_ia_en.txt
g "保監局 when:2d" gn_ia_zh2.txt
g "香港保險 when:1d" gn_hk_ins.txt
g "宏利 保險 when:2d" gn_manulife.txt
g "Manulife Hong Kong when:2d" gn_manulife_en.txt
g "香港保險業聯會 when:3d" gn_hkfi.txt
g "保險 香港 when:1d" gn_hkins2.txt
g "家族辦公室 when:2d" gn_fam.txt
g "保險科技 when:2d" gn_insurtech.txt
g "金融監管總局 保險 when:1d" gn_nfra.txt
g "insurtech Asia when:2d" gn_insurtech_en.txt
g "scmp insurance Hong Kong when:2d" gn_scmp.txt
g "友邦保險 when:2d" gn_aia.txt
echo DONE
