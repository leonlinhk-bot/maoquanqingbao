#!/usr/bin/env bash
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"
OUT=/Users/leonliang/maoquanqingbao/data/_cache1006_0049
t() { printf '%-26s ' "$1"; curl -sL -m 30 -A "$UA" -o "$OUT/$1" -w "%{http_code} %{size_download}\n" "$2"; }
t p_hkma_cargox.html "https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/10/20261005-3/"
t p_hkma_cargox2.html "https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/10/20261005-2/"
t p_govhk_cargox.html "https://www.info.gov.hk/gia/general/202610/05/P2026100500274.htm"
t p_scmp_schroders.html "https://www.scmp.com/business/banking-finance/article/3369699/asset-manager-schroders-expand-hong-kong-after-merger-nuve"
echo DONE
