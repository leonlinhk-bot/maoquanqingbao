#!/usr/bin/env python3
"""
Send digest report via Gmail SMTP.
Requires Gmail App Password (not regular password).
Setup: https://myaccount.google.com/apppasswords

Usage:
  # Set env var first (once):
  export GMAIL_APP_PASSWORD="xxxx xxxx xxxx xxxx"

  # Send daily digest:
  python3 scripts/send-digest.py --period daily --to weigangmaoquan@gmail.com

  # Send weekly digest:
  python3 scripts/send-digest.py --period weekly --to weigangmaoquan@gmail.com
"""
import json, os, smtplib, argparse, sys
from pathlib import Path
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent
FROM = "weigangmaoquan@gmail.com"
PASSWORD = os.environ.get("GMAIL_APP_PASSWORD", "")
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587

def tx(obj):
    if not obj: return ""
    if isinstance(obj, dict): return obj.get("sc", "") or obj.get("tc", "") or ""
    return str(obj)

def build_body(digest, period_label):
    """Build HTML email from digest entries."""
    lines = ["<html><body style='font-family:SF Pro Text,PingFang SC,sans-serif;max-width:640px;margin:0 auto;color:#1d1d1f'>"]
    lines.append(f"<h2 style='color:#c4a35a;margin-bottom:4px'>猫圈儿港险情报站 · {period_label}</h2>")
    lines.append(f"<p style='color:#888;font-size:13px;margin:0 0 20px'>{digest['date']} · 共 {digest.get('itemCount', 0)} 条导读</p>")
    
    items = digest.get("items", [])
    for idx, it in enumerate(items, 1):
        title = tx(it.get("title", ""))
        summary = tx(it.get("summary", ""))
        why = tx(it.get("why", ""))
        url = it.get("originalUrl", "")
        source = tx(it.get("source", ""))
        tier = it.get("sourceTier", "")
        lines.append(f"<div style='border-left:3px solid #c4a35a;padding:8px 0 8px 14px;margin:16px 0'>")
        lines.append(f"<h3 style='margin:0 0 6px;font-size:16px'>{idx}. {title}</h3>")
        lines.append(f"<p style='margin:0 0 6px;font-size:14px;color:#555'>{summary}</p>")
        if why:
            lines.append(f"<p style='margin:0 0 6px;font-size:13px;color:#888'>💡 {why}</p>")
        lines.append(f"<p style='margin:0;font-size:12px;color:#aaa'>{source} · <a href='{url}' style='color:#6cb6ff'>原文 →</a></p>")
        lines.append("</div>")
    
    lines.append("<hr style='border:0;border-top:1px solid #eee;margin:24px 0 12px'>")
    lines.append("<p style='font-size:11px;color:#bbb;text-align:center'>猫圈儿港险情报站 · 持牌人情报台<br/>")
    lines.append("专业分享 · 非销售邀约 · 以监管/保司原文为准<br/>")
    lines.append("<a href='https://hkmaoquanqingbao.com' style='color:#6cb6ff'>hkmaoquanqingbao.com</a></p>")
    lines.append("</body></html>")
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--period", default="daily", choices=["daily","weekly","monthly","yearly"])
    parser.add_argument("--to", default="weigangmaoquan@gmail.com")
    parser.add_argument("--dry-run", action="store_true", help="Print body to stdout, don't send")
    args = parser.parse_args()

    if not PASSWORD and not args.dry_run:
        print("ERROR: GMAIL_APP_PASSWORD not set.", file=sys.stderr)
        print("1. Go to https://myaccount.google.com/apppasswords", file=sys.stderr)
        print("2. Create an App Password for 'Mail' on 'Mac'", file=sys.stderr)
        print("3. Run: export GMAIL_APP_PASSWORD='xxxx xxxx xxxx xxxx'", file=sys.stderr)
        sys.exit(1)

    # Load data
    data = json.loads((ROOT / "data" / "live-items.json").read_text(encoding="utf-8"))
    digests = data.get("digests", {}).get(args.period, [])
    if not digests:
        print(f"No {args.period} digests found.")
        sys.exit(1)

    latest = digests[0]  # most recent
    date_str = tx(latest.get("label", ""))
    
    # Build full digest with items
    item_ids = latest.get("itemIds", [])
    item_map = {i["id"]: i for i in data["items"]}
    items = [item_map[iid] for iid in item_ids if iid in item_map]
    items.sort(key=lambda x: x.get("publishedAt", ""), reverse=True)

    digest_full = {
        "date": date_str,
        "itemCount": len(items),
        "items": items
    }
    body_html = build_body(digest_full, f"{args.period} digest")
    body_text = f"猫圈儿港险情报站 · {date_str}\n共 {len(items)} 条导读\n\n查看全文: https://hkmaoquanqingbao.com"

    if args.dry_run:
        print(body_html[:2000])
        return

    # Compose email
    msg = MIMEMultipart("alternative")
    msg["From"] = f"猫圈儿情报站 <{FROM}>"
    msg["To"] = args.to
    msg["Subject"] = f"猫圈儿港险情报站 · {args.period} digest · {date_str}"
    msg.attach(MIMEText(body_text, "plain", "utf-8"))
    msg.attach(MIMEText(body_html, "html", "utf-8"))

    # Send
    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login(FROM, PASSWORD)
            server.send_message(msg)
        print(f"✅ Sent {args.period} digest ({len(items)} items) to {args.to}")
    except smtplib.SMTPAuthenticationError:
        print("ERROR: Authentication failed. Is GMAIL_APP_PASSWORD correct?", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
