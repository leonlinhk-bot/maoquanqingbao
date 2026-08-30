#!/usr/bin/env python3
"""Deep-dive into downloaded HTML: find 2026-08 dated links / JSON blobs."""
import re, sys, html, glob, os

def hunt(path, pats):
    raw = open(path, encoding='utf-8', errors='replace').read()
    print(f'\n===== {os.path.basename(path)} ({len(raw)} bytes) =====')
    for pat in pats:
        hits = re.findall(pat, raw)
        print(f'--- pattern {pat[:40]}... hits={len(hits)}')
        for h in hits[:12]:
            if isinstance(h, tuple):
                h = ' | '.join(x.strip()[:80] for x in h)
            print('   ', h[:160])

if __name__ == '__main__':
    # AIA: press release links for 2026
    hunt('/tmp/probe_e9ca31.html', [
        r'href="([^"]*press-releases/2026[^"]*)"',
        r'([A-Za-z0-9\u4e00-\u9fff ]{10,80}2026年8月\d{1,2}日)',
    ])
    # Prudential: look for article JSON / news links
    hunt('/tmp/probe_f2a9e9.html', [
        r'"(?:url|href|path)"\s*:\s*"([^"]{20,120})"',
        r'([0-9]{4}-[0-9]{2}-[0-9]{2}[T ][^"]{0,60})',
    ])
    # Insurance Business Asia: article links
    hunt('/tmp/probe_6930a8.html', [
        r'href="(/asia/[^"]+)"[^>]*>([^<]{20,120})<',
        r'(20\d\d[-/]\d{1,2}[-/]\d{1,2})',
    ])
    # Sun Life: news links
    hunt('/tmp/probe_dce564.html', [
        r'href="([^"]*news[^"]*)"[^>]*>([^<]{15,120})<',
        r'(20\d\d[-/年.]\d{1,2}[-/月.]\d{1,2}[^<]{0,40})',
    ])
