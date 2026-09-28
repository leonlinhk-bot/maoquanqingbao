#!/usr/bin/env python3
"""
猫圈儿周报海报生成器（Pillow 渲染，1080×1350 朋友圈 4:5）
用法:
  python3 scripts/poster-weekly.py <config.json> [--out-dir DIR]

config.json schema:
{
  "kicker": "WEEKLY DIGEST",
  "title_pre": "周报摘要 · ",
  "title_hl": "2026-W39",
  "date_range": "9 月 21 日 — 9 月 27 日",
  "badge": "本周精选 13 条导读",
  "footer_count": "13",
  "items": [["条目标题", "一句话解读"], ...],
  "brand": "猫圈儿港险情报站",
  "brand_sub": "维港猫圈儿 · 持牌人情报台",
  "wx": "公众号：维港猫圈儿",
  "note": "专业参考 · 非销售/投资建议 · 数字请回原文",
  "domain": "hkmaoquanqingbao.com",
  "logo": "/Users/leonliang/maoquanqingbao/assets/logo-cat-256.jpg"
}
输出: <out-dir>/猫圈儿周报-<title_hl>-深色.png / -浅色.png
"""
import os, sys, json, argparse, re as _re
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1350
S = 2
CANVAS = (W * S, H * S)

FONT_SERIF = '/System/Library/Fonts/Supplemental/Songti.ttc'
FONT_PING  = '/System/Library/Fonts/PingFang.ttc'
if not os.path.exists(FONT_PING):
    FONT_PING = '/System/Library/Fonts/Hiragino Sans GB.ttc'

def pick(path, size, want_bold):
    best = (0, '')
    for i in range(14):
        try:
            f = ImageFont.truetype(path, size, index=i)
        except Exception:
            break
        nm = ' '.join([x for x in f.getname() if x])
        if any(k in nm for k in ('Bold', 'Heavy', 'W6', 'Black')) == want_bold:
            return i, nm
        best = (i, nm)
    return best

IDX_SERIF_B = pick(FONT_SERIF, 40, True)[0]
IDX_SERIF_R = pick(FONT_SERIF, 40, False)[0]
IDX_SANS_B  = pick(FONT_PING, 40, True)[0]
IDX_SANS_R  = pick(FONT_PING, 40, False)[0]

def F(family, size, bold=False):
    if family == 'serif':
        return ImageFont.truetype(FONT_SERIF, size * S, index=IDX_SERIF_B if bold else IDX_SERIF_R)
    return ImageFont.truetype(FONT_PING, size * S, index=IDX_SANS_B if bold else IDX_SANS_R)

THEMES = {
  'dark': {
    'bg': [(13,20,32), (10,14,20), (8,11,16)],
    'gold': (232,165,75),
    'ink': (238,242,248), 'ink_dim': (150,158,172), 'ink_faint': (104,112,126),
    'frame': (232,165,75,72), 'line': (232,165,75,56), 'itemline': (232,165,75,30),
  },
  'light': {
    'bg': [(250,247,240), (244,239,227), (239,232,216)],
    'gold': (182,152,90),
    'ink': (16,51,101), 'ink_dim': (86,111,148), 'ink_faint': (128,148,176),
    'frame': (16,51,101,44), 'line': (16,51,101,40), 'itemline': (16,51,101,24),
  },
}

def gradient(size, colors):
    w, h = size
    base = Image.new('RGB', (1, h))
    d = ImageDraw.Draw(base)
    for y in range(h):
        t = y / max(1, h - 1)
        pos = t * (len(colors) - 1)
        i = min(int(pos), len(colors) - 2)
        f = pos - i
        c0, c1 = colors[i], colors[i + 1]
        d.point((0, y), tuple(int(c0[k] + (c1[k] - c0[k]) * f) for k in range(3)))
    return base.resize((w, h), Image.BILINEAR)

# token 化换行：连续 ASCII（含 +/-/% 等）视为整体，避免 «+5.2%» «2,524» 被拆断
_TOKEN_RE = _re.compile(r'[A-Za-z0-9+\-][A-Za-z0-9+\-.,:%/]*|\s+|[^\s]')

def wrap(draw, text, font, maxw):
    tokens = _TOKEN_RE.findall(text)
    lines, line = [], ''
    for tk in tokens:
        if draw.textlength(line + tk, font=font) > maxw and line:
            lines.append(line); line = tk
        else:
            line += tk
    if line:
        lines.append(line)
    return lines

def circular_logo(path, size):
    img = Image.open(path).convert('RGBA').resize((size, size), Image.LANCZOS)
    mask = Image.new('L', (size, size), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size - 1, size - 1), fill=255)
    img.putalpha(mask)
    return img

def build(cfg, theme_name, out_path):
    C = THEMES[theme_name]
    img = gradient(CANVAS, C['bg']).convert('RGBA')
    d = ImageDraw.Draw(img, 'RGBA')
    P = lambda v: v * S

    # 顶部金线（两端渐隐）
    fade = Image.new('RGBA', (CANVAS[0], P(8)), (0, 0, 0, 0))
    fd = ImageDraw.Draw(fade)
    for x in range(CANVAS[0]):
        t = x / CANVAS[0]
        a = int(255 * (t / .28)) if t < .28 else (int(255 * ((1 - t) / .28)) if t > .72 else 255)
        fd.line([(x, 0), (x, P(8))], fill=C['gold'] + (max(0, min(255, a)),))
    img.alpha_composite(fade, (0, 0))

    d.rectangle([P(26), P(26), CANVAS[0] - P(26), CANVAS[1] - P(26)], outline=C['frame'], width=P(2))

    MX = P(88)
    RIGHT = CANVAS[0] - P(88)
    y = P(74)

    # 品牌行
    logo = cfg.get('logo')
    if logo and os.path.exists(logo):
        try:
            lg = circular_logo(logo, P(52))
            img.paste(lg, (MX, y), lg)
            d.ellipse([MX - P(1), y - P(1), MX + P(53), y + P(53)], outline=C['gold'], width=P(2))
        except Exception as e:
            print('logo fail:', e)
    d.text((MX + P(70), y + P(4)), cfg.get('brand', ''), font=F('sans', 26, True), fill=C['gold'])
    d.text((MX + P(70), y + P(42)), cfg.get('brand_sub', ''), font=F('sans', 14, False), fill=C['ink_faint'])
    y += P(96)

    # 标题区
    d.text((MX, y), cfg.get('kicker', ''), font=F('sans', 15, False), fill=C['gold'])
    y += P(34)
    f_title = F('serif', 63, True)
    t1, t2 = cfg.get('title_pre', ''), cfg.get('title_hl', '')
    d.text((MX, y), t1, font=f_title, fill=C['ink'])
    w1 = d.textlength(t1, font=f_title)
    d.text((MX + w1, y), t2, font=f_title, fill=C['gold'])
    y += P(84)

    f_range, f_cnt = F('sans', 22, False), F('sans', 16, False)
    d.text((MX, y), cfg.get('date_range', ''), font=f_range, fill=C['ink_dim'])
    wr = d.textlength(cfg.get('date_range', ''), font=f_range) + P(18)
    d.text((MX + wr, y + P(7)), cfg.get('badge', ''), font=f_cnt, fill=C['gold'])
    y += P(56)
    d.line([MX, y, RIGHT, y], fill=C['line'], width=P(1))
    y += P(40)

    # 条目
    f_num, f_it, f_id = F('serif', 40, True), F('sans', 29, True), F('sans', 20, False)
    TXT_X = MX + P(112)
    TXT_W = RIGHT - TXT_X
    items = cfg.get('items', [])

    measured = []
    for title, desc in items:
        tl = wrap(d, title, f_it, TXT_W)[:2]
        dl = wrap(d, desc, f_id, TXT_W)
        measured.append((tl, dl, len(tl) * P(40) + P(8) + len(dl) * P(33)))

    foot_line_y = P(H) - P(60) - P(96)
    avail = foot_line_y - y - P(24)
    total_h = sum(h for _, _, h in measured)
    gap = max(P(18), int((avail - total_h) / max(1, len(measured) - 0.35)))

    for idx, (tl, dl, h) in enumerate(measured, 1):
        d.text((MX, y - P(2)), f"{idx:02d}", font=f_num, fill=C['gold'])
        yy = y
        for ln in tl:
            d.text((TXT_X, yy), ln, font=f_it, fill=C['ink']); yy += P(40)
        yy += P(8)
        for ln in dl:
            d.text((TXT_X, yy), ln, font=f_id, fill=C['ink_dim']); yy += P(33)
        y = yy + gap
        if idx < len(measured):
            d.line([MX, y - gap // 2, RIGHT, y - gap // 2], fill=C['itemline'], width=P(1))

    # 页脚
    fy = P(H) - P(60)
    d.line([MX, fy - P(96), RIGHT, fy - P(96)], fill=C['line'], width=P(1))
    d.text((MX, fy - P(74)), cfg.get('domain', ''), font=F('sans', 27, True), fill=C['gold'])
    d.text((MX, fy - P(30)), cfg.get('note', ''), font=F('sans', 14, False), fill=C['ink_faint'])

    s1, s2, s3 = "本周共 ", cfg.get('footer_count', ''), " 条导读"
    f_dig, f_num2 = F('sans', 19, False), F('sans', 23, True)
    dx = RIGHT - (d.textlength(s1, font=f_dig) + d.textlength(s2, font=f_num2) + d.textlength(s3, font=f_dig))
    d.text((dx, fy - P(72)), s1, font=f_dig, fill=C['ink_dim']); dx += d.textlength(s1, font=f_dig)
    d.text((dx, fy - P(76)), s2, font=f_num2, fill=C['gold']); dx += d.textlength(s2, font=f_num2)
    d.text((dx, fy - P(72)), s3, font=f_dig, fill=C['ink_dim'])
    f_wx = F('sans', 14, False)
    wx_t = cfg.get('wx', '')
    d.text((RIGHT - d.textlength(wx_t, font=f_wx), fy - P(30)), wx_t, font=f_wx, fill=C['ink_faint'])

    out = img.convert('RGB').resize((W, H), Image.LANCZOS)
    out.save(out_path, 'PNG', optimize=True)
    print("saved", out_path, out.size)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('config')
    ap.add_argument('--out-dir', default=os.path.expanduser('~/Downloads'))
    a = ap.parse_args()
    cfg = json.load(open(a.config, encoding='utf-8'))
    os.makedirs(a.out_dir, exist_ok=True)
    tag = cfg.get('title_hl', 'weekly')
    for theme, label in (('dark', '深色'), ('light', '浅色')):
        build(cfg, theme, os.path.join(a.out_dir, f"猫圈儿周报-{tag}-{label}.png"))

if __name__ == '__main__':
    main()
