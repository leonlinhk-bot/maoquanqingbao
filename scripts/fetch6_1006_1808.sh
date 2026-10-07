#!/bin/bash
cd /Users/leonliang/maoquanqingbao
OUT=data/_raw_1006_1808
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
fetch() {
  curl -sSL --noproxy '*' --max-time 45 -A "$UA" "$2" -o "$OUT/$1" -w "%{http_code} %{size_download} $1\n" || echo "FAIL $1"
}
fetch art_fo.html "https://insuranceasia.com/news/digital-tokens-eye-tax-exempt-status-singapore-reviews-family-office-list"
fetch art_msig.html "https://insuranceasia.com/insurance/news/msig-extends-fire-cover-over-300-orang-asli-homes"
fetch art_aon.html "https://insuranceasia.com/insurance/news/aon-strengthens-japan-network-two-leadership-appointments"
fetch art_india.html "https://insuranceasia.com/insurance/in-focus/india-insurance-growth-fails-widen-life-coverage"
fetch art_meritz.html "https://insuranceasianews.com/meritz-moving-to-sell-51-stake-in-indonesian-jv-report/"
fetch art_pruism.html "https://insuranceasianews.com/prudential-agrees-us5bn-reinsurance-deal-with-prismic-life/"
fetch art_hdi.html "https://www.insurancebusinessmag.com/asia/news/professional-liability/hdi-global-expands-medical-malpractice-into-global-healthcare-unit-592443.aspx"
fetch hkb_sitemap.xml "https://hongkongbusiness.hk/sitemap.xml"
fetch nfra_items.html "https://www.nfra.gov.cn/cn/view/pages/ItemListRightList.html?itemPId=923&itemId=915"
echo DONE
