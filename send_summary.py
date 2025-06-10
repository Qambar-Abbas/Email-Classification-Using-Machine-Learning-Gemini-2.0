import smtplib
from email.mime.text import MIMEText
import requests

def send_email(summary_text, to="you@example.com"):
    msg = MIMEText(summary_text)
    msg["Subject"] = "Your Daily Inbox Summary"
    msg["From"] = "bot@example.com"
    msg["To"] = to

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("your_email@gmail.com", "app_password")
    server.sendmail(msg["From"], [msg["To"]], msg.as_string())
    server.quit()

def send_to_slack(text, webhook_url):
    requests.post(webhook_url, json={"text": text})
