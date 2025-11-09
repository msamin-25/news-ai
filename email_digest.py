# email_digest.py — Send email with top news summaries

import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv
from news_api import fetch_news
from nlp import summarize_text

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def send_digest(recipient, category="technology", limit=3):
    """Send a daily email digest with summarized news"""
    articles = fetch_news(category=category, page_size=limit)
    if not articles:
        return "No articles to send."

    summaries = []
    for a in articles:
        title = a["title"]
        summary = summarize_text(a.get("description", ""))
        summaries.append(f"📌 {title}\\n➡ {summary}\\n{a['url']}\\n")

    body = "\\n\\n".join(summaries)
    msg = MIMEText(body)
    msg["Subject"] = f"Your Daily {category.title()} News Digest"
    msg["From"] = EMAIL_USER
    msg["To"] = recipient

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, recipient, msg.as_string())
        server.quit()
        return "Email sent successfully!"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print(send_digest("test@example.com"))
