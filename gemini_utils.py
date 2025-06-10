# gemini_utils.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# 1️⃣ List available models on import (for debugging)
def list_available_models():
    print("Fetching available Gemini models...")
    models = genai.list_models()
    for m in models:
        # Only print model names that support text generation
        if m.supported_generation_methods:
            print(f"  • {m.name} : methods={m.supported_generation_methods}")

# Run this once to see what you can use
list_available_models()

# 2️⃣ Pick a valid model name (e.g. text-bison or chat-bison)
#    Change this if you want chat-bison or another.
# MODEL_NAME = "models/gemini-1.5-flash"
MODEL_NAME = "models/gemini-2.0-flash"
model = genai.GenerativeModel(MODEL_NAME)

def classify_email(email):
    prompt = f"""
You are an assistant for classifying short sales emails.
Classify into one of: hot lead, follow-up, ignore.

Email:
Subject: {email['subject']}
From: {email['from']}
Body:
{email['body'][:1000]}

Respond with exactly one word: hot lead, follow-up, or ignore.
"""
    resp = model.generate_content(prompt)
    return resp.text.strip().lower()

def summarize_emails(emails):
    prompt = "Summarize these emails into bullet points with suggested next actions:\n\n"
    for e in emails:
        prompt += f"[{e['label'].upper()}] {e['subject']} from {e['from']}\n{e['body'][:300]}\n\n"
    prompt += "Output bullet points like:\n- [LABEL] Subject: Next action"
    resp = model.generate_content(prompt)
    return resp.text.strip()
