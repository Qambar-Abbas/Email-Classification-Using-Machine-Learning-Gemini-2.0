from display_summary import display_summary
from gmail_utils import authenticate_gmail, fetch_recent_emails
from gemini_utils import classify_email, summarize_emails


def main():
    service = authenticate_gmail()
    emails = fetch_recent_emails(service, max_results=10)
    for e in emails:
        e["label"] = classify_email(e)

    summary = summarize_emails(emails)
    print(summary)

    # choose one:
    # send_email(summary, to="qambarabbas54325@gmail.com")
    # OR
    # send_to_slack(summary, webhook_url="https://hooks.slack.com/services/XXX")
    # OR
    display_summary(emails)

if __name__ == "__main__":
    main()
