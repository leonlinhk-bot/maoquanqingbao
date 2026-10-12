#!/usr/bin/env bash
cd /Users/leonliang/maoquanqingbao/.cache1012_1818
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
for u in "https://www.nfra.gov.cn/cn/view/pages/ItemList.html?itemPId=923&itemId=931&itemUrl=ItemListRightList.html&itemName=%E7%9B%91%E7%AE%A1%E5%8A%A8%E6%80%81" ; do
  curl -sL -m 25 -A "$UA" -o nfra_list.html -w "nfra_list %{http_code} %{size_download}\n" "$u"
done
curl -sL -m 25 -A "$UA" -o nfra_api.json -w "nfra_api %{http_code} %{size_download}\n" "https://www.nfra.gov.cn/cn/view/pages/ItemList.html?itemPId=923"
# hkma in-focus / other
curl -sL -m 25 -A "$UA" -o hkma_infocus.html -w "hkma_infocus %{http_code} %{size_download}\n" "https://www.hkma.gov.hk/eng/news-and-media/insight/"
echo done
