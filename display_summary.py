import webbrowser
import os

def display_summary(emails, output_path="summary.html"):
    """
    Displays a summary of emails in a styled HTML page using cards.

    :param emails: List of email summaries. Each item should be a dict with keys: 'subject', 'sender', 'snippet', 'label'
    :param output_path: Output HTML file path
    """
    html_content = """
    <html>
    <head>
        <title>Email Summary</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                padding: 20px;
            }
            .container {
                display: flex;
                flex-wrap: wrap;
                gap: 20px;
            }
            .card {
                background-color: white;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                padding: 20px;
                width: 300px;
                transition: transform 0.2s;
            }
            .card:hover {
                transform: scale(1.02);
            }
            .label {
                font-size: 12px;
                font-weight: bold;
                padding: 4px 8px;
                background-color: #2196f3;
                color: white;
                border-radius: 5px;
                display: inline-block;
                margin-bottom: 10px;
            }
            .subject {
                font-size: 18px;
                font-weight: bold;
                margin: 10px 0;
            }
            .sender {
                font-size: 14px;
                color: #888;
                margin-bottom: 10px;
            }
            .snippet {
                font-size: 14px;
                color: #333;
            }
        </style>
    </head>
    <body>
        <h1>Your Email Summary</h1>
        <div class="container">
    """

    for email in emails:
        html_content += f"""
            <div class="card">
                <div class="label">{email.get('label', 'Uncategorized')}</div>
                <div class="subject">{email.get('subject', 'No Subject')}</div>
                <div class="sender">From: {email.get('sender', 'Unknown')}</div>
                <div class="snippet">{email.get('snippet', 'No content available...')}</div>
            </div>
        """

    html_content += """
        </div>
    </body>
    </html>
    """

    # Write to file
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    # Open in browser
    abs_path = os.path.abspath(output_path)
    webbrowser.open(f"file://{abs_path}")
