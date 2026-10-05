#!/usr/bin/env python3
"""
猫圈儿情报站 · 介绍长图海报生成器（Pillow 渲染，宽 1080，高度按内容动态计算）
用法:
  python3 scripts/poster-intro.py <config.json> [--out-dir DIR]

config.json schema:
{
  "kicker": "WHY IFA READ THIS",
  "title_line1": "为什么 IFA 都在看",
  "title_line2": "猫圈儿港险情报站",
  "subtitle": "...",
  "blocks": [
    {"tag":"视角一 · 省时间", "head":"...", "lead":"...",
     "list_title":"...", "bullets":["...","..."], "closing":"..."}
  ],
  "matrix_title": "它能给 IFA 带来什么",
  "matrix": [["痛点","给什么"], ...],
  "closing_big": "不漏 · 有据 · 有底气",
  "closing_note": "...",
  "brand":"...", "brand_sub":"...", "wx":"...", "note":"...", "domain":"...", "logo":"..."
}
输出: <out-dir>/猫圈儿情报站介绍-深色.png / -浅色.png
"""
import os, sys, json, argparse, re as _re
from PIL import Image, ImageDraw, ImageFont

S = 2                      # 超采样倍数
W = 1080                   # 输出宽度
CANVAS_W = W * S
PAD = 88 * S               # 左右边距
PAD_TOP = 78 * S

FONT_SERIF = '/System/Library/Fonts/Supplemental/Songti.ttc'
FONT_PING  = '/System/Library/Fonts/PingFang.ttc'
FONT_MONO  = '/System/Library/Fonts/Menlo.ttc'
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
        'bg': [(13, 20, 32), (10, 14, 20), (8, 11, 16)],
        'gold': (232, 165, 75),
        'ink': (238, 242, 248), 'ink_dim': (150, 158, 172), 'ink_faint': (104, 112, 126),
        'frame': (232, 165, 75, 72), 'line': (232, 165, 75, 56), 'itemline': (232, 165, 75, 30),
        'card': (255, 255, 255, 10), 'cardline': (232, 165, 75, 34),
    },
    'light': {
        'bg': [(250, 247, 240), (244, 239, 227), (239, 232, 216)],
        'gold': (182, 152, 90),
        'ink': (16, 51, 101), 'ink_dim': (86, 111, 148), 'ink_faint': (128, 148, 176),
        'frame': (16, 51, 101, 44), 'line': (16, 51, 101, 40), 'itemline': (16, 51, 101, 24),
        'card': (255, 255, 255, 150), 'cardline': (16, 51, 101, 30),
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


# ── 中文换行：token 化 + 数字单位 binding + widow 均衡 + 行首禁则 ──
_TOKEN_RE = _re.compile(r'[A-Za-z0-9+\-][A-Za-z0-9+\-.,:%/]*|\s+|[^\s]')
_CN_CHAR = _re.compile(r'[\u4e00-\u9fff]$')


def _merge_units(tokens):
    out, i, n = [], 0, len(tokens)
    while i < n:
        tk = tokens[i]
        if _re.match(r'^[A-Za-z0-9+\-]', tk) and _re.search(r'[0-9]', tk):
            j, buf, cnt = i + 1, tk, 0
            while j < n and cnt < 2:
                nxt = tokens[j]
                if nxt.strip() == '':
                    if j + 1 < n and _CN_CHAR.match(tokens[j + 1]):
                        buf += nxt; j += 1; continue
                    break
                if _CN_CHAR.match(nxt):
                    buf += nxt; j += 1; cnt += 1; continue
                break
            out.append(buf); i = j; continue
        out.append(tk); i += 1
    return out


def wrap(draw, text, font, maxw):
    tokens = _merge_units(_TOKEN_RE.findall(text))
    lines, line = [], ''
    for tk in tokens:
        if draw.textlength(line + tk, font=font) > maxw and line:
            lines.append(line); line = tk
        else:
            line += tk
    if line:
        lines.append(line)
    if len(lines) < 2:
        return lines
    min_last = maxw * 0.30
    guard = 0
    while guard < 60:
        if draw.textlength(lines[-1], font=font) >= min_last:
            break
        prev_tokens = _merge_units(_TOKEN_RE.findall(lines[-2]))
        if len(prev_tokens) <= 1:
            break
        tk = prev_tokens[-1]
        if draw.textlength(tk + lines[-1], font=font) > maxw:
            break
        lines[-2] = ''.join(prev_tokens[:-1])
        lines[-1] = tk + lines[-1]
        guard += 1
    if not lines[-2] or not lines[-1]:
        lines = [l for l in lines if l]
    _NO_START = '。，、；：？！）〕】》」』〉·'
    for i in range(1, len(lines)):
        while len(lines[i]) > 1 and lines[i][0] in _NO_START:
            lines[i - 1] += lines[i][0]
            lines[i] = lines[i][1:]
    return lines


def circular_logo(path, size):
    img = Image.open(path).convert('RGBA').resize((size, size), Image.LANCZOS)
    mask = Image.new('L', (size, size), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size - 1, size - 1), fill=255)
    img.putalpha(mask)
    return img


# ── 排版度量 ──
LH_BODY   = 34 * S     # 正文行高
LH_BULLET = 33 * S
LH_HEAD   = 46 * S
LH_SMALL  = 29 * S
FS_BODY   = 21
FS_BULLET = 20
FS_HEAD   = 29
FS_TAG    = 16
FS_MATRIX = 18


def layout(cfg, C, img=None):
    """绘制并返回总高度（img=None 时仅测量）。"""
    d = ImageDraw.Draw(img) if img is not None else ImageDraw.Draw(Image.new('RGB', (8, 8)))
    X = PAD
    RIGHT = CANVAS_W - PAD
    CW = RIGHT - X
    y = PAD_TOP

    def line(txt, font, fill, lh, x=None):
        nonlocal y
        if img is not None:
            d.text((X if x is None else x, y), txt, font=font, fill=fill)
        y += lh

    def para(txt, font, fill, lh, x=None, w=None):
        nonlocal y
        lines = wrap(d, txt, font, w if w else CW)
        for ln in lines:
            if img is not None:
                d.text((X if x is None else x, y), ln, font=font, fill=fill)
            y += lh
        return len(lines)

    # ── 品牌行 ──
    logo = cfg.get('logo')
    if img is not None and logo and os.path.exists(logo):
        try:
            lg = circular_logo(logo, 52 * S)
            img.paste(lg, (X, y), lg)
            d.ellipse([X - S, y - S, X + 53 * S, y + 53 * S], outline=C['gold'], width=2 * S)
        except Exception as e:
            print('logo fail:', e)
    if img is not None:
        d.text((X + 70 * S, y + 4 * S), cfg.get('brand', ''), font=F('sans', 26, True), fill=C['gold'])
        d.text((X + 70 * S, y + 42 * S), cfg.get('brand_sub', ''), font=F('sans', 14, False), fill=C['ink_faint'])
    y += 96 * S

    # ── 标题区 ──
    line(cfg.get('kicker', ''), F('sans', 15, False), C['gold'], 34 * S)
    f_t = F('serif', 56, True)
    line(cfg.get('title_line1', ''), f_t, C['ink'], 74 * S)
    line(cfg.get('title_line2', ''), f_t, C['gold'], 84 * S)
    line(cfg.get('subtitle', ''), F('sans', 20, False), C['ink_dim'], 42 * S)
    y += 6 * S
    if img is not None:
        d.line([X, y, RIGHT, y], fill=C['line'], width=S)
    y += 40 * S

    # ── 正文区块 ──
    f_tag  = F('sans', FS_TAG, True)
    f_head = F('sans', FS_HEAD, True)
    f_body = F('sans', FS_BODY, False)
    f_bul  = F('sans', FS_BULLET, False)
    f_bulb = F('sans', FS_BULLET, True)

    for bi, blk in enumerate(cfg.get('blocks', [])):
        if img is not None:
            # 卡片底
            pass
        line(blk.get('tag', ''), f_tag, C['gold'], 30 * S)
        para(blk.get('head', ''), f_head, C['ink'], LH_HEAD)
        y += 8 * S
        para(blk.get('lead', ''), f_body, C['ink_dim'], LH_BODY)
        y += 10 * S
        if blk.get('list_title'):
            para(blk.get('list_title', ''), f_bulb, C['ink'], LH_BULLET)
            y += 4 * S
        for b in blk.get('bullets', []):
            bx = X + 30 * S
            if img is not None:
                d.text((X + 2 * S, y + 2 * S), '▸', font=f_bulb, fill=C['gold'])
            lines = wrap(d, b, f_bul, CW - 30 * S)
            for ln in lines:
                if img is not None:
                    d.text((bx, y), ln, font=f_bul, fill=C['ink_dim'])
                y += LH_BULLET
            y += 5 * S
        y += 6 * S
        paras = para(blk.get('closing', ''), f_bulb, C['gold'], LH_BULLET)
        y += 46 * S
        if img is not None and bi < len(cfg.get('blocks', [])) - 1:
            d.line([X, y - 26 * S, RIGHT, y - 26 * S], fill=C['itemline'], width=S)

    # ── 矩阵 ──
    if cfg.get('matrix'):
        line(cfg.get('matrix_title', ''), f_head, C['ink'], LH_HEAD + 8 * S)
        y += 10 * S
        LCOL = 330 * S
        RCOL = CW - LCOL - 28 * S
        for left, right in cfg['matrix']:
            ll = wrap(d, left, f_body, LCOL)
            rl = wrap(d, right, f_body, RCOL)
            h = max(len(ll), len(rl)) * LH_SMALL + 22 * S
            if img is not None:
                yy = y
                for ln in ll:
                    d.text((X, yy), ln, font=f_body, fill=C['ink_dim']); yy += LH_SMALL
                yy = y
                for ln in rl:
                    d.text((X + LCOL + 28 * S, yy), ln, font=f_body, fill=C['ink']); yy += LH_SMALL
                d.line([X, y + h - 10 * S, RIGHT, y + h - 10 * S], fill=C['itemline'], width=S)
            y += h
        y += 30 * S

    # ── 收束 ──
    if img is not None:
        d.line([X, y, RIGHT, y], fill=C['line'], width=S)
    y += 44 * S
    line(cfg.get('closing_big', ''), F('serif', 40, True), C['gold'], 62 * S)
    para(cfg.get('closing_note', ''), f_body, C['ink_dim'], LH_BODY)
    y += 40 * S

    # ── 页脚 ──
    if img is not None:
        d.line([X, y, RIGHT, y], fill=C['line'], width=S)
    y += 30 * S
    if img is not None:
        d.text((X, y), cfg.get('domain', ''), font=F('sans', 27, True), fill=C['gold'])
        wx_t = cfg.get('wx', '')
        d.text((RIGHT - d.textlength(wx_t, font=F('sans', 15, False)), y + 4 * S), wx_t,
               font=F('sans', 15, False), fill=C['ink_dim'])
    y += 44 * S
    if img is not None:
        d.text((X, y), cfg.get('note', ''), font=F('sans', 14, False), fill=C['ink_faint'])
    y += 34 * S
    return y


def build(cfg, theme_name, out_path):
    C = THEMES[theme_name]
    # pass 1: 测量
    H_s = int(layout(cfg, C, None)) + 40 * S
    canvas = (CANVAS_W, H_s)
    # pass 2: 渲染
    img = gradient(canvas, C['bg']).convert('RGBA')
    d = ImageDraw.Draw(img, 'RGBA')

    # 顶部金线（两端渐隐）
    fade = Image.new('RGBA', (CANVAS_W, 8 * S), (0, 0, 0, 0))
    fd = ImageDraw.Draw(fade)
    for x in range(CANVAS_W):
        t = x / CANVAS_W
        a = int(255 * (t / .28)) if t < .28 else (int(255 * ((1 - t) / .28)) if t > .72 else 255)
        fd.line([(x, 0), (x, 8 * S)], fill=C['gold'] + (max(0, min(255, a)),))
    img.alpha_composite(fade, (0, 0))

    d.rectangle([26 * S, 26 * S, CANVAS_W - 26 * S, H_s - 26 * S], outline=C['frame'], width=2 * S)

    layout(cfg, C, img)
    out = img.convert('RGB').resize((W, int(H_s / S)), Image.LANCZOS)
    out.save(out_path, 'PNG', optimize=True)
    print("saved", out_path, out.size)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('config')
    ap.add_argument('--out-dir', default=os.path.expanduser('~/Downloads'))
    a = ap.parse_args()
    cfg = json.load(open(a.config, encoding='utf-8'))
    os.makedirs(a.out_dir, exist_ok=True)
    tag = cfg.get('out_tag', '介绍')
    for theme, label in (('dark', '深色'), ('light', '浅色')):
        build(cfg, theme, os.path.join(a.out_dir, f"猫圈儿情报站-{tag}-{label}.png"))


if __name__ == '__main__':
    main()
