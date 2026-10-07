#!/usr/bin/env python3
"""
信息源字段清污（只做 key 合并）。

用法:
  python3 scripts/cleanup-sources.py            # 预览（dry-run）
  python3 scripts/cleanup-sources.py --apply    # 写回 live-items.json

背景：source.sc 由入库时自由生成（833 个唯一值、格式漂移），sourceKey 从中派生，
      导致同一媒体分叉成多个 key（insurancebusiness / insurancebusinessmag 等），
      信源统计失真。本脚本只合并「明确同义」的 key。

⚠️ 2026-10-08 教训 —— 不要对 source.sc 做「去日期」式文本清污：
  实测同一类来源会一半带日期、一半不带（`Artemis 2026-10-06 報道` 被清成 `Artemis`，
  而 `Artemis 2026-10-05` 原样保留）→ 造成**新的不一致**；且被删的日期与备注其实有
  溯源价值（如「大纪元转载《明报》2026-10-03 16:18」「[EN原文，待核原文]」，
  还有「据 FSS 数据、首尔经济日报与 SBS 报道」这类多源交叉信息）。
  正确方向是「结构化」而非「删除」——把 source 拆成 name / date / note 三字段，
  属于分类体系改动，须先出方案再动手（见 docs/ 方案稿）。
"""
import json, sys, collections, shutil, datetime, os

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


def main():
    apply = '--apply' in sys.argv
    d = json.load(open(P, encoding='utf-8'))
    items = d['items']

    key_changes = collections.Counter()
    for i in items:
        k = i.get('sourceKey')
        if k in KEY_MERGE:
            key_changes[f"{k} → {KEY_MERGE[k]}"] += 1
            if apply:
                i['sourceKey'] = KEY_MERGE[k]

    print("=== sourceKey 合并（明确同义）===")
    for k, v in key_changes.most_common():
        print(f"  {k:42s} {v} 条")
    print(f"  合计 {sum(key_changes.values())} 条")
    print("\n（source.sc 文本不做清污——理由见脚本头部 2026-10-08 教训）")

    if apply:
        bak = P + '.bak-keys-' + datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        shutil.copy(P, bak)
        json.dump(d, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(f"\n✔ 已写回（备份 {os.path.basename(bak)}）")
    else:
        print("\n（预览模式，未写回。加 --apply 执行）")


if __name__ == '__main__':
    main()
