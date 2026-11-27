#!/usr/bin/env python3
"""
IA 监管文档监视器 —— 用「列表页 diff」而不是新闻来找新文档

为什么这样做（2026-11 实测）：
  IA 的 **列表页直连可抓**（HTTP 200，真实内容），而新闻稿页是 JS 空壳。
  所以不必猜 PDF 文件名（命名不统一，纯枚举会漏），直接盯列表页：
    · 通函  /en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_{YEAR}.html
    · 指引  /en/legislative_framework/guidelines.html
  每次抓取 → 与上次快照对比 → 只报新增项。完整覆盖，零猜测。

用法：
  python3 scripts/ia-doc-watch.py            # 检查新增（首次运行建立基线）
  python3 scripts/ia-doc-watch.py --all      # 打印全部条目
  python3 scripts/ia-doc-watch.py --years 2024,2025,2026

输出：
  data/_ia_docs/snapshot.json   上次快照
  data/_ia_docs/latest.json     本次抓取结果
  终端：新增条目清单（含 PDF 直链）
"""
import json
import os
import re
import subprocess
import sys
from datetime import date

OUT_DIR = "data/_ia_docs"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0 Safari/537.36")
IA = "https://www.ia.org.hk"
CIRC_URL = IA + "/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_{y}.html"
GL_URL = IA + "/en/legislative_framework/guidelines.html"


def fetch(url):
    """直连抓取（绕开坏掉的本机代理）。返回 HTML 或 None。"""
    r = subprocess.run(
        ["curl", "--noproxy", "*", "-sL", "-m", "30", "-A", UA, url],
        capture_output=True, text=True,
    )
    if r.returncode != 0 or not r.stdout or len(r.stdout) < 2000:
        return None
    if "Just a moment" in r.stdout or "challenge-platform" in r.stdout:
        return None
    return r.stdout


def clean(s):
    s = re.sub(r"<[^>]+>", "", s)
    s = s.replace("&nbsp;", " ").replace("&amp;", "&").replace("&ldquo;", "“").replace("&rdquo;", "”")
    return re.sub(r"\s+", " ", s).strip()


def parse_circulars(html, year):
    """从通函列表页提取 [(date, subject, pdf_url, attachments)]

    注意：一行里可能有多个 PDF（主通函 + 附件），例 2026-05-29 那行是
    Cir_dd_29.05.2026.pdf 加 20260529_Annex.pdf。附件往往才是实质内容，
    只取第一个会漏掉整份报告，所以这里全收。
    """
    out = []
    for row in re.findall(r"<tr[^>]*>(.*?)</tr>", html, re.S):
        cells = re.findall(r"<td[^>]*>(.*?)</td>", row, re.S)
        if len(cells) < 2:
            continue
        d, s = clean(cells[0]), clean(cells[1])
        if not d or not s or d.lower().startswith("date"):
            continue
        hrefs = re.findall(r'href="([^"]+\.pdf)"', row, re.I)
        urls = []
        for h in hrefs:
            if h.startswith("http"):
                urls.append(h)
            elif h.startswith("/"):
                urls.append(IA + h)
            else:
                urls.append(IA + "/en/legislative_framework/circulars/reg_matters/" + h)
        if not urls:
            continue
        out.append({
            "kind": "circular",
            "year": year,
            "date": d,
            "subject": s,
            "pdf": urls[0],
            "attachments": urls[1:],
        })
    return out


def parse_guidelines(html):
    """从指引页提取 [(ref, title, pdf_url)]

    注意：指引页是单列表格，编号写在 <a> 的文字里而不是单独一列；
    而且文件名不总是 GLxx.pdf（例：GL20 → files/Guideline_on_Cybersecurity_English.pdf），
    所以必须从链接文字解析编号，不能靠文件名。
    """
    out = []
    for m in re.finditer(r'<a[^>]+href="([^"]+\.pdf)"[^>]*>(.*?)</a>', html, re.S | re.I):
        href, text = m.group(1), clean(m.group(2))
        gm = re.match(r"(GL\s?\d+[A-Z]?)\s*[:\-—]?\s*(.*)", text, re.I)
        if not gm:
            continue
        ref = gm.group(1).replace(" ", "").upper()
        title = gm.group(2).strip() or text
        if href.startswith("http"):
            pdf = href
        elif href.startswith("/"):
            pdf = IA + href
        else:
            pdf = IA + "/en/legislative_framework/" + href
        out.append({"kind": "guideline", "ref": ref, "subject": title, "pdf": pdf})
    return out


def collect(years):
    docs = []
    for y in years:
        html = fetch(CIRC_URL.format(y=y))
        if html:
            got = parse_circulars(html, y)
            print(f"  通函 {y}: {len(got)} 条")
            docs += got
        else:
            print(f"  通函 {y}: 抓取失败")
    html = fetch(GL_URL)
    if html:
        got = parse_guidelines(html)
        print(f"  指引: {len(got)} 条")
        docs += got
    else:
        print("  指引: 抓取失败")
    return docs


def key(d):
    return d.get("pdf") or f'{d["kind"]}|{d.get("date") or d.get("ref")}|{d["subject"]}'


def main():
    args = sys.argv[1:]
    show_all = "--all" in args
    years = [date.today().year, date.today().year - 1]
    for a in args:
        if a.startswith("--years"):
            val = a.split("=", 1)[1] if "=" in a else args[args.index(a) + 1]
            years = [int(x) for x in val.split(",")]

    os.makedirs(OUT_DIR, exist_ok=True)
    print(f"抓取 IA 文档索引（通函年份: {years}）…")
    docs = collect(sorted(years, reverse=True))
    print(f"共 {len(docs)} 条")

    latest_path = os.path.join(OUT_DIR, "latest.json")
    snap_path = os.path.join(OUT_DIR, "snapshot.json")

    old = {}
    if os.path.exists(snap_path):
        try:
            old = {key(d): d for d in json.load(open(snap_path))}
        except Exception:
            old = {}

    new_items = [d for d in docs if key(d) not in old]

    json.dump(docs, open(latest_path, "w"), ensure_ascii=False, indent=1)
    json.dump(docs, open(snap_path, "w"), ensure_ascii=False, indent=1)

    if show_all:
        print("\n=== 全部条目 ===")
        for d in docs:
            tag = d.get("date") or d.get("ref")
            print(f"  [{d['kind']}] {tag} — {d['subject'][:70]}")
    elif not old:
        print("\n（首次运行，已建立基线。下次起只报新增。）")
    elif new_items:
        print(f"\n=== 🔔 发现 {len(new_items)} 条新文档 ===")
        for d in new_items:
            tag = d.get("date") or d.get("ref")
            print(f"  [{d['kind']}] {tag} — {d['subject'][:75]}")
            if d.get("pdf"):
                print(f"       主文档: {d['pdf']}")
            for a in d.get("attachments") or []:
                print(f"       附件:   {a}")
            # 直接给出可复制的抓取命令
            urls = ([d["pdf"]] if d.get("pdf") else []) + list(d.get("attachments") or [])
            if urls:
                print(f"       抓取:   python3 scripts/ia-pdf-fetch.py " + " ".join(f'"{u}"' for u in urls))
    else:
        print("\n（无新增）")


if __name__ == "__main__":
    main()
