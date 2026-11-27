#!/usr/bin/env python3
"""
IA 通函 PDF 抓取器

背景（2026-11 实测）：
  ia.org.hk 的 **HTML 页面**被 Cloudflare JS 挑战挡住（cf_chl），curl / headless 浏览器 /
  curl_cffi TLS 指纹 / Jina / DeepSeek fetch / Wayback 全部失败，连 robots.txt 与 sitemap 都 403。
  但 **PDF 文件直链可以直接下载**（HTTP 200），前提是：
    ① 知道确切文件名  ② 走直连（本机代理会把它挡成 000）

用法：
  python3 scripts/ia-pdf-fetch.py <pdf_url> [<pdf_url> ...]
      下载指定 PDF → 提取文本 → 列出文中引用的其他 IA PDF（可作为追踪线索）

  python3 scripts/ia-pdf-fetch.py --scan [N]
      扫描最近 N 天（默认 14）的 cir_dd_DD.MM.YYYY.pdf 命名

输出：
  data/_ia_pdfs/<文件名>.pdf      原始文件
  data/_ia_pdfs/<文件名>.txt      提取的文本
  终端打印摘要 + 交叉引用
"""
import os
import re
import subprocess
import sys
from datetime import date, timedelta

BASE = "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/files"
OUT_DIR = "data/_ia_pdfs"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0 Safari/537.36")


def fetch(url, dest):
    """直连下载（不读系统代理）。返回 True/False。"""
    r = subprocess.run(
        ["curl", "--noproxy", "*", "-sL", "-m", "40", "-A", UA,
         "-o", dest, "-w", "%{http_code}", url],
        capture_output=True, text=True,
    )
    code = (r.stdout or "").strip()
    return code == "200" and os.path.exists(dest) and os.path.getsize(dest) > 5000


def extract_text(pdf_path, txt_path):
    """用 PyMuPDF 提取文本。返回文本或 None。"""
    try:
        import fitz
    except ImportError:
        print("  [!] 需要 PyMuPDF：python3 -m pip install pymupdf")
        return None
    doc = fitz.open(pdf_path)
    text = "\n".join(p.get_text() for p in doc)
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(text)
    return text


def cross_refs(text):
    """抽出文中引用的其他 IA PDF 链接。"""
    urls = re.findall(r"https?://www\.ia\.org\.hk/[^\s\)\]\"']+?\.pdf", text, re.I)
    seen, out = set(), []
    for u in urls:
        key = u.lower()
        if key not in seen:
            seen.add(key)
            out.append(u)
    return out


def handle(url):
    name = url.rstrip("/").split("/")[-1]
    os.makedirs(OUT_DIR, exist_ok=True)
    pdf = os.path.join(OUT_DIR, name)
    txt = os.path.join(OUT_DIR, name.replace(".pdf", ".txt"))

    print(f"\n=== {name} ===")
    if os.path.exists(pdf) and os.path.getsize(pdf) > 5000:
        print(f"  已存在，跳过下载（{os.path.getsize(pdf):,} bytes）")
    elif fetch(url, pdf):
        print(f"  ✅ 下载成功 {os.path.getsize(pdf):,} bytes")
    else:
        print("  ❌ 下载失败（可能文件名不对，或代理未绕过）")
        return

    text = extract_text(pdf, txt)
    if not text:
        return
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    print(f"  文本 {len(lines)} 行，存至 {txt}")
    # 打印头 12 行（通常是日期 / ref / 收件人 / 主题）
    for l in lines[:12]:
        print("   |", l[:100])

    refs = cross_refs(text)
    if refs:
        print(f"  → 文中引用 {len(refs)} 个 IA PDF（可继续追踪）：")
        for r in refs:
            print("     ", r)


def scan(days=14):
    """扫描最近 N 天的 cir_dd_DD.MM.YYYY.pdf"""
    print(f"扫描最近 {days} 天的 cir_dd_DD.MM.YYYY.pdf 命名…")
    found = []
    today = date.today()
    for i in range(days):
        d = today - timedelta(days=i)
        fname = f"cir_dd_{d.day:02d}.{d.month:02d}.{d.year}.pdf"
        url = f"{BASE}/{fname}"
        r = subprocess.run(
            ["curl", "--noproxy", "*", "-s", "-o", "/dev/null", "-w", "%{http_code}",
             "-m", "8", "-A", UA, url],
            capture_output=True, text=True,
        )
        if (r.stdout or "").strip() == "200":
            found.append(url)
            print(f"  ✅ {d.isoformat()}  {fname}")
    if not found:
        print("  （无命中）")
    else:
        print(f"\n发现 {len(found)} 个，开始下载：")
        for u in found:
            handle(u)


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return
    if args[0] == "--scan":
        scan(int(args[1]) if len(args) > 1 else 14)
    else:
        for u in args:
            handle(u)


if __name__ == "__main__":
    main()
