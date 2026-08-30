#!/bin/bash
# Resolve Google News redirect URLs to canonical article URLs + content via r.jina.ai
cd /tmp || exit 1
resolve() {
  local url="$1" out="$2"
  curl -s --max-time 45 "https://r.jina.ai/$url" -o "$out"
  echo "== $out ($(wc -c < "$out" | tr -d ' '))"
  grep -m1 "URL Source" "$out"
}
resolve "https://news.google.com/rss/articles/CBMimANBVV95cUxPbWZoNndFTXlmTzRENFhDMnptMkYtZ2xDNmN3aV9DZHhiODJ1SVlHdFhJU285SEpFXy1pZW1GUEZ6TkduY0phTGxLYkd2V0RjRDVhaFA5TVB" j_hket_manu.txt
resolve "https://news.google.com/rss/articles/CBMi5gFBVV95cUxNSl9POXhRNlNzOEI2aHozSzB0ZFZkcWgycDVocGV1T1BzaG9BVFpOUFJkWGhPT3dGVElBOTczdmhpSDl4WmhMN0VCemdyYS11NHl5aFVTekx" j_hket_aia.txt
resolve "https://news.google.com/rss/articles/CBMihgNBVV95cUxNVUJrWUw1UVpXWHVYeG1LLTVjSmZ6UkpLakFTcUZyd2R0OUdidGhzOE53c25aa0k3NkY5UEZOMkZpTVhpZFhLM1dyUDByWGNUSGxSc1FFQ0l" j_sunlife_ai.txt
resolve "https://news.google.com/rss/articles/CBMixwJBVV95cUxNZGNEQ1B4S244WXVzejA1ZFlCX21aYlJGTUlxVlJvNjF3R3NhQlhiUUlwS0ZzMUVqbFRDbHR1NjdiYUF3UWMxZE5pMDRFZDB3NTBkbFVoNUN" j_hket_gold.txt
