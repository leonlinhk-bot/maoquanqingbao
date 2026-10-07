#!/usr/bin/env python3
"""
source 字段结构化（方案 A 保守版）。

- 新增  source.name / source.date / source.note
- `sc` / `tc` 显示字段【一个字不动】→ 前端零变化、零风险
- sourceKey 改为从 `name` 稳定派生（映射由现有数据「投票」学习，不臆造新 key）
- 解析不确定时：整体留在 name，date/note 留空 —— 不猜

用法:
  python3 scripts/structure-sources.py           # dry-run（看解析质量）
  python3 scripts/structure-sources.py --apply   # 写回
"""
import json, re, sys, os, collections, shutil, datetime

P = '/Users/leonliang/maoquanqingbao/data/live-items.json'

BRACKET = re.compile(r'[\[［]([^\]］]{1,60})[\]］]')
DATE_TAIL = re.compile(
    r'\s*(?:[（(]\s*(\d{4}-\d{2}-\d{2})(?:\s+\d{1,2}:\d{2})?\s*[）)]'
    r'|(\d{4}-\d{2}-\d{2})(?:\s+\d{1,2}:\d{2})?)'
    r'\s*(?:報道|报道)?\s*$')
REPORT_TAIL = re.compile(r'\s*(?:報道|报道)\s*$')
SPLIT_WORD = re.compile(r'(转载|转自|据|另见|参考|引述)')
NOTE_KEYWORDS = ('待核', '原文', '转载', '另见', '据', '引述', '注', '综合')


def parse(sc):
    """sc 自由文本 → (name, date, note)"""
    s = (sc or '').strip()
    if not s:
        return '', None, None
    notes = []

    # 1) 方括号备注（只取含关键词的，避免误伤「（香港）」这类限定词）
    for m in list(BRACKET.finditer(s)):
        inner = m.group(1).strip()
        if any(k in inner for k in NOTE_KEYWORDS):
            notes.append(inner)
            s = s.replace(m.group(0), '')

    # 2) 「转载/据/另见」之后的部分归入 note（避免把复合来源留在 name 里）
    m = SPLIT_WORD.search(s)
    if m and m.start() >= 2:
        notes.append(s[m.start():].strip())
        s = s[:m.start()].strip()

    # 3) 尾部日期
    date = None
    m = DATE_TAIL.search(s)
    if m:
        date = m.group(1) or m.group(2)
        s = s[:m.start()]

    s = REPORT_TAIL.sub('', s).strip()
    s = re.sub(r'[\s·・，,、；;：:]+$', '', s).strip()

    name = s or (sc or '').strip()      # 保底：解析失败就用原文
    note = '；'.join(n for n in notes if n) or None
    return name, date, note


def norm(x):
    return re.sub(r'[^a-z0-9\u4e00-\u9fff]', '', (x or '').lower())


def main():
    apply = '--apply' in sys.argv
    d = json.load(open(P, encoding='utf-8'))
    items = d['items']

    samples, changed = [], 0
    name_votes = collections.defaultdict(collections.Counter)

    for i in items:
        src = i.get('source')
        if not isinstance(src, dict):
            continue
        sc = src.get('sc') or ''
        name, date, note = parse(sc)
        if len(samples) < 14:
            samples.append((sc, name, date, note))
        if name != sc or date or note:
            changed += 1
        if apply:
            src['name'] = name
            src['date'] = date
            src['note'] = note
        if name and i.get('sourceKey'):
            name_votes[norm(name)][i['sourceKey']] += 1

    MAP = {n: c.most_common(1)[0][0] for n, c in name_votes.items()}
    key_fix = 0
    if apply:
        for i in items:
            src = i.get('source') or {}
            nm = src.get('name') or ''
            k = MAP.get(norm(nm))
            if k and k != i.get('sourceKey'):
                i['sourceKey'] = k
                key_fix += 1

    print("=== 解析样例（sc → name | date | note）===")
    for sc, nm, dt, nt in samples:
        print(f"  「{sc[:50]}」")
        print(f"     → name=「{nm[:38]}」 date={dt} note=「{(nt or '')[:38]}」")

    multi = sum(1 for n, c in name_votes.items() if len(c) > 1)
    print(f"\n=== 统计 ===")
    print(f"  可结构化的条目: {changed} / {len(items)}")
    print(f"  name 唯一值: {len(name_votes)}（原 sc 唯一值 833）")
    print(f"  同一 name 曾对应多个 key 的: {multi} 组 ← 这些会被规范化")
    if apply:
        print(f"  sourceKey 修正: {key_fix} 条")
        bak = P + '.bak-struct-' + datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        shutil.copy(P, bak)
        json.dump(d, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(f"  ✔ 已写回（备份 {os.path.basename(bak)}）")
    else:
        print("\n（dry-run，未写回）")


if __name__ == '__main__':
    main()
