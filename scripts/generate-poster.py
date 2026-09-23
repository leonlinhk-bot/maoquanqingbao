#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate WeChat moments poster from daily intel data."""
import json, sys, datetime, subprocess, os

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "..", "assets", "poster-template.html")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "posters")

def load_top_items(n=4):
    """Load top N items: prefer recent (last 3 days) by score, fill with all-time top score."""
    data_path = os.path.join(os.path.dirname(__file__), "..", "data", "live-items.json")
    with open(data_path) as f:
        data = json.load(f)
    items = data["items"]
    today = datetime.date.today()
    cutoff = (today - datetime.timedelta(days=2)).isoformat()

    def pub_date(it):
        return (it.get("publishedAt") or "")[:10]

    recent = [it for it in items if pub_date(it) >= cutoff]
    # 当日条目优先（海报=「当日」朋友圈发布物），其余按分数回填，避免两日前的高分旧条目长期霸榜
    today_s = today.isoformat()
    recent.sort(key=lambda x: (pub_date(x) == today_s, x.get("score", 0), pub_date(x)), reverse=True)
    picked = recent[:n]
    if len(picked) < n:
        seen = {x.get("id") for x in picked}
        rest = [it for it in items if it.get("id") not in seen]
        rest.sort(key=lambda x: x.get("score", 0), reverse=True)
        picked += rest[: n - len(picked)]
    return picked

def gen_card(item):
    """Generate HTML card for one item"""
    t = item.get("title", {}).get("sc", "")
    s = item.get("summary", {}).get("sc", "")[:100]
    w = item.get("why", {}).get("sc", "")[:40]
    source = item.get("source", {}).get("sc", "")
    boards = item.get("boards", [])
    board = boards[0] if boards else "regulatory"
    
    board_map = {
        "reg": "🏛 监管", "regulatory": "🏛 监管", "compliance": "⚖ 合规",
        "product": "📦 产品", "insurer": "🏢 保司", "firm": "🏢 保司",
        "market": "📊 市场", "family": "🏛 家办", "cross": "🌏 跨境",
        "tech": "🤖 科技", "macro": "📊 宏观", "intl": "🌍 国际",
        "channel": "👥 渠道", "offshore": "🏝 离岸"
    }
    tag = board_map.get(board, "📌 资讯")
    
    return f"""<div class="card">
<div class="meta">
<span class="tag">{tag}</span>
<span class="source-name">{source}</span>
</div>
<h3>{t}</h3>
<p>{s}</p>
<div class="action-hint">→ {w}</div>
</div>"""

def generate(today=None):
    if today is None:
        today = datetime.date.today()
    
    items = load_top_items(4)
    
    with open(TEMPLATE_PATH) as f:
        html = f.read()
    
    # Replace date
    weekdays = ["一","二","三","四","五","六","日"]
    wd = weekdays[today.weekday()]
    html = html.replace(">29<", f">{today.day}<")
    html = html.replace("7月 · 星期三", f"{today.month}月 · 星期{wd}")
    
    # Replace cards
    cards_html = "\n".join(gen_card(it) for it in items)
    # Find the cards div and replace content
    import re
    pattern = r'(<div class="cards">)(.*?)(</div>\s*<div class="footer">)'
    replacement = rf'\1\n{cards_html}\n        \3'
    html = re.sub(pattern, replacement, html, flags=re.DOTALL)
    
    # Save
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    poster_path = os.path.join(OUTPUT_DIR, f"poster-{today}.html")
    with open(poster_path, "w") as f:
        f.write(html)
    
    print(f"✅ 海报生成: {poster_path}")
    print(f"   包含 {len(items)} 条精选导读")
    return poster_path

if __name__ == "__main__":
    poster = generate()
