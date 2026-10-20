#!/usr/bin/env bash
cd /Users/leonliang/maoquanqingbao/.cache1020_1808
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
g() { curl -sL -m 40 -A "$UA" -o "$1" -w "$1 %{http_code} %{size_download}\n" "$2"; }
g air97221.html "https://www.asiainsurancereview.com/News/View-NewsLetter-Article/id/97221/Type/AirPlus/Hong-Kong-Life-insurance-market-expected-to-expand-by-5-10-" &
g air97220.html "https://www.asiainsurancereview.com/News/View-NewsLetter-Article/id/97220/Type/AirPlus/Hong-Kong-Five-Year-Plan-unlocks-insurance-opportunities-but-insurers-need-to-manage-underlying-risks" &
g air97259.html "https://www.asiainsurancereview.com/News/View-NewsLetter-Article/id/97259/Type/eCin/Regulator-cracks-down-on-quick-returns-life-products" &
g air97257.html "https://www.asiainsurancereview.com/News/View-NewsLetter-Article/id/97257/Type/eCin/NFRA-revises-insurance-product-development-and-management-regulations" &
g iaasia_sunlife.html "https://insuranceasia.com/insurance/news/sunlife-adopts-new-global-branding" &
g ian_cyclone.html "https://insuranceasianews.com/australias-cyclone-pool-cuts-up-to-37-of-home-insurance-premiums-in-high-risk-areas/" &
g ian_howden.html "https://insuranceasianews.com/a-lot-of-hunger-to-grow-strong-reinsurer-results-drive-further-apac-softening-howden-res-souter-says/" &
g ia_indonesia.html "https://insuranceasia.com/insurance/in-focus/indonesia-insurers-face-profit-squeeze-despite-stable-outlook" &
g ia_taiwan.html "https://insuranceasia.com/insurance/news/taiwan-approves-full-health-insurance-subsidies-seniors" &
g ia_hdfc.html "https://insuranceasia.com/insurance/news/hdfc-life-lifts-new-business-value-15-122m" &
wait
echo done
