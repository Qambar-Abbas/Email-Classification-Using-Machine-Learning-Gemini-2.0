import base64, email
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

def authenticate_gmail():
    flow = InstalledAppFlow.from_client_secrets_file(
        "credentials.json", scopes=SCOPES
    )
    creds = flow.run_local_server(port=0)
    return build("gmail", "v1", credentials=creds)

def get_email_body(payload):
    if "data" in payload.get("body", {}):
        return base64.urlsafe_b64decode(payload["body"]["data"]).decode("utf-8", errors="ignore")
    for part in payload.get("parts", []):
        if part.get("mimeType") == "text/plain" and "data" in part.get("body", {}):
            return base64.urlsafe_b64decode(part["body"]["data"]).decode("utf-8", errors="ignore")
    return ""

def fetch_recent_emails(service, max_results=10):
    results = service.users().messages().list(
        userId="me", maxResults=max_results
    ).execute()
    messages = results.get("messages", [])
    emails = []
    for msg in messages:
        data = service.users().messages().get(
            userId="me", id=msg["id"], format="full"
        ).execute()
        headers = {h["name"]: h["value"] for h in data["payload"]["headers"]}
        emails.append({
            "subject": headers.get("Subject", ""),
            "from": headers.get("From", ""),
            "body": get_email_body(data["payload"])
        })
    return emails
