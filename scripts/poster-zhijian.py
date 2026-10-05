#!/usr/bin/env python3
"""
智见 · AI 港险观察 周报海报生成器（Pillow，AI 科技风，1080×1350）
与母刊 poster-weekly.py 同体系但差异化：青为主调 + 科技元素（网格/节点/准星/等宽序号），金退为点缀。

用法:
  python3 scripts/poster-zhijian.py <config.json> [--out-dir DIR]

config.json schema:
{
  "title_pre": "智见 · ", "title_hl": "AI", "title_post": " 港险观察",
  "kicker": "▸ WEEKLY AI DIGEST",
  "date_range": "9 月 21 日 — 9 月 27 日",
  "badge": "周报摘要 2026-W39 · 本周精选 5 条",
  "footer_prefix": "源自 ", "footer_num": "12", "footer_suffix": " 条公开信源",
  "brand": "猫圈儿港险情报站", "brand_sub": "维港猫圈儿 · 持牌人情报台",
  "wx": "公众号：维港猫圈儿",
  "note": "专业参考 · 非销售/投资建议 · 数字请回原文",
  "domain": "hkmaoquanqingbao.com",
  "logo": "/Users/leonliang/maoquanqingbao/assets/logo-cat-256.jpg",
  "items": [["标题", "解读"], ...]
}
输出: <out-dir>/智见AI港险观察-<日期标识>-深色.png / -浅色.png
"""
import os, json, argparse, re as _re
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1350
S = 2
CANVAS = (W * S, H * S)

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
IDX_MONO_R  = pick(FONT_MONO, 40, False)[0]
IDX_MONO_B  = pick(FONT_MONO, 40, True)[0]


def F(family, size, bold=False):
    if family == 'serif':
        return ImageFont.truetype(FONT_SERIF, size * S, index=IDX_SERIF_B if bold else IDX_SERIF_R)
    if family == 'mono':
        return ImageFont.truetype(FONT_MONO, size * S, index=IDX_MONO_B if bold else IDX_MONO_R)
    return ImageFont.truetype(FONT_PING, size * S, index=IDX_SANS_B if bold else IDX_SANS_R)


# 青为主调，金退为品牌点缀
THEMES = {
  'dark': {
    'bg': [(6,10,20), (11,19,36), (5,9,17)],
    'accent': (34,211,238), 'accent2': (94,234,212), 'gold': (232,165,75),
    'ink': (232,240,250), 'ink_dim': (144,164,188), 'ink_faint': (96,114,138),
    'grid': (34,211,238,15), 'frame': (34,211,238,60),
    'line': (34,211,238,52), 'itemline': (34,211,238,28),
    'node': (34,211,238,95), 'nodecore': (34,211,238,190),
  },
  'light': {
    'bg': [(245,249,254), (232,240,250), (245,249,254)],
    'accent': (8,145,178), 'accent2': (13,148,136), 'gold': (176,146,86),
    'ink': (11,43,87), 'ink_dim': (74,101,136), 'ink_faint': (124,144,170),
    'grid': (14,116,144,20), 'frame': (14,116,144,52),
    'line': (14,116,144,44), 'itemline': (14,116,144,26),
    'node': (14,116,144,80), 'nodecore': (14,116,144,170),
  },
}

_TOKEN_RE = _re.compile(r'[A-Za-z0-9+\-][A-Za-z0-9+\-.,:%/]*|\s+|[^\s]')
_CN_CHAR = _re.compile(r'[\u4e00-\u9fff]$')


def _merge_units(tokens):
    """数字与其后的中文单位（最多 2 字，可含空格）binding 成一个 token，
    避免「30 学时」「49 亿元」这类被换行拆开。"""
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


def wrap(draw, text, font, maxw):
    """token 化换行：连续 ASCII（+5.2% / 2,524）不可拆，中文逐字；并避免 widow（末行孤短）。"""
    lines, line = [], ''
    for tk in _merge_units(_TOKEN_RE.findall(text)):
        if draw.textlength(line + tk, font=font) > maxw and line:
            lines.append(line); line = tk
        else:
            line += tk
    if line:
        lines.append(line)
    if len(lines) < 2:
        return lines
    # 末行过短时，把上一行末尾的 token 依次搬到末行做均衡（避免「负责」被拆且末行孤短）
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
    # 行首禁则：中文标点不得出现在行首（回搬至上一行末，允许标点悬挂）
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


def draw_grid(img, color, step):
    layer = Image.new('RGBA', img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    for x in range(0, img.size[0], step):
        for y in range(0, img.size[1], step):
            d.point((x, y), fill=color)
    img.alpha_composite(layer)


def draw_nodes(img, cx, cy, C, scale=1.0):
    layer = Image.new('RGBA', img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    pts = [(-58,-34), (4,-52), (64,-22), (74,30), (10,58), (-60,28)]
    pts = [(int(cx + x * scale), int(cy + y * scale)) for x, y in pts]
    for i in range(len(pts)):
        for j in (i + 1, i + 3):
            if j < len(pts):
                d.line([pts[i], pts[j]], fill=C['node'], width=max(1, int(2 * scale)))
    r = max(2, int(4 * scale))
    for p in pts:
        d.ellipse([p[0]-r, p[1]-r, p[0]+r, p[1]+r], fill=C['nodecore'])
    img.alpha_composite(layer)


def corner_marks(d, C, inset=26, ln=34, wd=3):
    P = lambda v: v * S
    for x, y, sx, sy in [(inset, inset, 1, 1), (W-inset, inset, -1, 1),
                         (inset, H-inset, 1, -1), (W-inset, H-inset, -1, -1)]:
        d.line([P(x), P(y), P(x + sx * ln), P(y)], fill=C['accent2'], width=P(wd))
        d.line([P(x), P(y), P(x), P(y + sy * ln)], fill=C['accent2'], width=P(wd))


def build(cfg, theme_name, out_path):
    C = THEMES[theme_name]
    img = gradient(CANVAS, C['bg']).convert('RGBA')
    draw_grid(img, C['grid'], 40 * S)
    d = ImageDraw.Draw(img, 'RGBA')
    P = lambda v: v * S

    # 顶部金→青渐变线（母刊金过渡到 AI 青）
    top = Image.new('RGBA', (CANVAS[0], P(6)), (0, 0, 0, 0))
    td = ImageDraw.Draw(top)
    GOLD, CYAN = C['gold'], C['accent']
    for x in range(CANVAS[0]):
        t = x / CANVAS[0]
        a = 255 if 0.18 < t < 0.82 else int(255 * (min(t, 1 - t) / 0.18))
        cr = int(GOLD[0] + (CYAN[0] - GOLD[0]) * t)
        cg = int(GOLD[1] + (CYAN[1] - GOLD[1]) * t)
        cb = int(GOLD[2] + (CYAN[2] - GOLD[2]) * t)
        td.line([(x, 0), (x, P(6))], fill=(cr, cg, cb, max(0, min(255, a))))
    img.alpha_composite(top, (0, 0))

    d.rectangle([P(26), P(26), CANVAS[0] - P(26), CANVAS[1] - P(26)], outline=C['frame'], width=P(2))
    corner_marks(d, C)

    MX = P(88)
    RIGHT = CANVAS[0] - P(88)
    y = P(74)

    # 品牌行（logo 保持金色圈：母刊锚点）
    logo = cfg.get('logo')
    if logo and os.path.exists(logo):
        try:
            lg = circular_logo(logo, P(52))
            img.paste(lg, (MX, y), lg)
            d.ellipse([MX - P(1), y - P(1), MX + P(53), y + P(53)], outline=C['gold'], width=P(2))
        except Exception as e:
            print('logo fail:', e)
    d.text((MX + P(70), y + P(4)), cfg.get('brand', ''), font=F('sans', 26, True), fill=C['ink'])
    d.text((MX + P(70), y + P(42)), cfg.get('brand_sub', ''), font=F('sans', 14, False), fill=C['ink_faint'])
    draw_nodes(img, RIGHT - P(78), y + P(26), C, scale=S * 0.40)
    y += P(96)

    # 标题区
    d.text((MX, y), cfg.get('kicker', ''), font=F('mono', 14, True), fill=C['accent'])
    y += P(36)
    f_title = F('serif', 63, True)
    t1, t2, t3 = cfg.get('title_pre', ''), cfg.get('title_hl', ''), cfg.get('title_post', '')
    d.text((MX, y), t1, font=f_title, fill=C['ink'])
    w1 = d.textlength(t1, font=f_title)
    d.text((MX + w1, y), t2, font=f_title, fill=C['accent'])
    w2 = d.textlength(t2, font=f_title)
    d.text((MX + w1 + w2, y), t3, font=f_title, fill=C['ink'])
    d.rectangle([MX, y + P(78), MX + P(120), y + P(82)], fill=C['accent'])
    y += P(92)

    f_range, f_cnt = F('sans', 21, False), F('sans', 15, False)
    dr = cfg.get('date_range', '')
    d.text((MX, y), dr, font=f_range, fill=C['ink_dim'])
    wr = d.textlength(dr, font=f_range) + P(18)
    d.text((MX + wr, y + P(6)), cfg.get('badge', ''), font=f_cnt, fill=C['accent'])
    y += P(54)
    d.line([MX, y, RIGHT, y], fill=C['line'], width=P(1))
    y += P(40)

    # 条目（动态均分间距）
    f_num, f_it, f_id = F('mono', 30, True), F('sans', 29, True), F('sans', 20, False)
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
        # 序号：等宽数字 + 左侧青色竖条
        d.rectangle([MX, y + P(4), MX + P(5), y + P(38)], fill=C['accent'])
        d.text((MX + P(16), y), f"{idx:02d}", font=f_num, fill=C['accent'])
        yy = y
        for ln in tl:
            d.text((TXT_X, yy), ln, font=f_it, fill=C['ink']); yy += P(40)
        yy += P(8)
        for ln in dl:
            d.text((TXT_X, yy), ln, font=f_id, fill=C['ink_dim']); yy += P(33)
        y = yy + gap
        if idx < len(measured):
            ly = y - gap // 2
            d.line([MX, ly, MX + P(150), ly], fill=C['accent2'], width=P(2))
            xh = MX + P(162)
            while xh < RIGHT:
                d.line([xh, ly, xh + P(6), ly], fill=C['itemline'], width=P(1))
                xh += P(14)

    # 页脚
    fy = P(H) - P(60)
    d.line([MX, fy - P(96), RIGHT, fy - P(96)], fill=C['line'], width=P(1))
    d.text((MX, fy - P(74)), cfg.get('domain', ''), font=F('sans', 27, True), fill=C['gold'])
    d.text((MX, fy - P(30)), cfg.get('note', ''), font=F('sans', 14, False), fill=C['ink_faint'])

    s1, s2, s3 = cfg.get('footer_prefix', ''), cfg.get('footer_num', ''), cfg.get('footer_suffix', '')
    f_dig, f_num2 = F('sans', 16, False), F('mono', 20, True)
    dx = RIGHT - (d.textlength(s1, font=f_dig) + d.textlength(s2, font=f_num2) + d.textlength(s3, font=f_dig))
    d.text((dx, fy - P(72)), s1, font=f_dig, fill=C['ink_dim']); dx += d.textlength(s1, font=f_dig)
    d.text((dx, fy - P(76)), s2, font=f_num2, fill=C['accent']); dx += d.textlength(s2, font=f_num2)
    d.text((dx, fy - P(72)), s3, font=f_dig, fill=C['ink_dim'])
    f_wx = F('sans', 14, False)
    wx_t = cfg.get('wx', '')
    d.text((RIGHT - d.textlength(wx_t, font=f_wx), fy - P(30)), wx_t, font=f_wx, fill=C['ink_faint'])

    # 左下渐隐方块数据条
    for i in range(8):
        alpha = max(25, 210 - i * 26)
        d.rectangle([MX + i * P(12), fy - P(4), MX + i * P(12) + P(7), fy + P(3)],
                    fill=C['accent'][:3] + (alpha,))

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
    tag = cfg.get('tag', 'weekly')
    for theme, label in (('dark', '深色'), ('light', '浅色')):
        build(cfg, theme, os.path.join(a.out_dir, f"智见AI港险观察-{tag}-{label}.png"))


if __name__ == '__main__':
    main()
