#!/usr/bin/env bash
mkdir -p .cache1014_0058
cd .cache1014_0058
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
for pair in "914 915" "920 923" "921 924" "922 925" "937 938" "916 917"; do
  set -- $pair
  curl -sL -m 30 -A "$UA" -o "nfra_$1_$2.json" "https://www.nfra.gov.cn/cn/view/pages/ItemList.json?itemPId=$1&itemId=$2" 2>/dev/null
  echo "nfra_$1_$2.json $(wc -c < nfra_$1_$2.json | tr -d ' ')"
done
echo done
