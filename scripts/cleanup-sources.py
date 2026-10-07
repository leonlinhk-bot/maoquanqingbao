#!/usr/bin/env python3
"""
信息源字段清污：规范化 source.sc（去机器标记）+ 合并同义 sourceKey。
用法:
  python3 scripts/cleanup-sources.py            # 预览（dry-run）
  python3 scripts/cleanup-sources.py --apply    # 写回 live-items.json

背景：source.sc 由入库时自由生成（833 个唯一值、格式漂移），sourceKey 从中派生，
      导致同一媒体分叉成多个 key、同义 key 并存，信源统计失真。
只做「清污」（去噪声、合并同义），不改分类语义——语义定义需另行拍板。
"""
import json, re, sys, collections, shutil, datetime, os

P = '/Users/leonliang/maoquanqingbao/data/live-items.json'

# 明确同义的 key 合并（左=脏值，右=规范值）
KEY_MERGE = {
    'insurancebusiness': 'insurancebusinessmag',
    'InsuranceAsia': 'insuranceasia',
    'InsuranceAsiaNews': 'insuranceasianews',
    'chinalife': 'china-life',
    'chinlife': 'china-life',
    'ctf-life': 'ctflife',
    'axa-hk': 'axa',
    'prudential-hk': 'prudential',
    'hkma_press': 'hkma',
    '港交所 HKEX': 'hkex',
    'mof-sta': 'mof',
}

# source.sc 的机器标记（去噪声，不动机构名本身）
PATTERNS = [
    (re.compile(r'（\d{4}-\d{2}-\d{2}）\s*\[\s*EN原文\s*\]'), ''),
    (re.compile(r'\(\d{4}-\d{2}-\d{2}\)\s*\[\s*EN原文\s*\]'), ''),
    (re.compile(r'\s*\[\s*EN原文\s*\]\s*'), ''),
    (re.compile(r'\s*\d{4}-\d{2}-\d{2}\s*報道\s*$'), ''),
    (re.compile(r'\s*\d{4}-\d{2}-\d{2}\s*报道\s*$'), ''),
    (re.compile(r'\s*·\s*\d{4}年\d{1,2}月\d{1,2}日\s*$'), ''),
    (re.compile(r'\s*（\d{4}-\d{2}-\d{2}）\s*$'), ''),
    (re.compile(r'\s*\(\d{4}-\d{2}-\d{2}\)\s*$'), ''),
]


def clean(s):
    orig = s
    for pat, rep in PATTERNS:
        s = pat.sub(rep, s)
    s = re.sub(r'\s{2,}', ' ', s).strip()
    return s


def main():
    apply = '--apply' in sys.argv
    d = json.load(open(P, encoding='utf-8'))
    items = d['items']

    key_changes = collections.Counter()
    sc_pairs = []
    sc_changed = 0
    for i in items:
        k = i.get('sourceKey')
        if k in KEY_MERGE:
            key_changes[f"{k} → {KEY_MERGE[k]}"] += 1
            if apply:
                i['sourceKey'] = KEY_MERGE[k]
        src = i.get('source')
        if not isinstance(src, dict):
            continue
        for lang in ('sc', 'tc'):
            v = src.get(lang)
            if not v:
                continue
            nv = clean(v)
            if nv != v:
                if lang == 'sc':
                    sc_changed += 1
                    if len(sc_pairs) < 15:
                        sc_pairs.append((v, nv))
                if apply:
                    src[lang] = nv

    print("=== sourceKey 合并 ===")
    for k, v in key_changes.most_common():
        print(f"  {k:42s} {v} 条")
    print(f"  合计 {sum(key_changes.values())} 条\n")

    print("=== source.sc 规范化 ===")
    print(f"  改动 {sc_changed} 条（sc 字段）")
    for a, b in sc_pairs:
        print(f"    「{a[:52]}」 → 「{b[:52]}」")

    if apply:
        bak = P + '.bak-clean-' + datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        shutil.copy(P, bak)
        # meta.changelog 记录
        meta = d.setdefault('meta', {})
        meta.setdefault('changelog', []).insert(0, {
            "date": datetime.date.today().isoformat(),
            "title": {"sc": "信息源字段清污", "tc": "信息源欄位清污"},
            "items": [
                f"合并同义 sourceKey {sum(key_changes.values())} 条",
                f"规范化 source.sc 机器标记 {sc_changed} 条（去日期/EN标记噪声）",
            ],
        })
        json.dump(d, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(f"\n✔ 已写回（备份 {os.path.basename(bak)}）")
    else:
        print("\n（预览模式，未写回。加 --apply 执行）")


if __name__ == '__main__':
    main()
