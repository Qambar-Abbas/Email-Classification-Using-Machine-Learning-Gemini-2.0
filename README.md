# Inbox Classifier

A simple, open-source Python tool that:

1. Fetches your latest Gmail messages  
2. Classifies each as **hot lead**, **follow-up**, or **ignore/vendor** using Google Gemini 2.0  
3. Summarizes actionable tasks in a beautiful HTML “card” view  
4. Opens the summary in your browser  

Everyone is welcome to use, learn from, and contribute to this project!

---

## 1. Project Structure

Here’s how the files and folders are organized. Think of each line as a branch on a tree:

```
inbox_cleaner/              ← Project root folder
├── environment.yml         ← Conda environment spec (Python, dependencies)
├── requirements.txt        ← pip dependencies
├── .env                    ← Your SECRET keys (not committed)
├── credentials.json        ← Gmail OAuth client info
├── gmail_utils.py          ← Fetch & parse Gmail messages
├── gemini_utils.py         ← Call Gemini for classification & summarization
├── display_summary.py      ← Build HTML & open in browser
├── inbox_cleaner.py        ← Main script: coordinates everything
└── README.md               ← This file
```

---

## 2. Setup & Run (Step-by-Step)

Follow these steps exactly—no prior experience needed:

1. **Clone the repo**  
   ```bash
   git clone https://github.com/QambarOfficial/inbox_cleaner.git
   cd inbox-cleaner
   ```

2. **Add secrets**  
   - Copy your Gmail OAuth file into `credentials.json`.  
   - Create a file named `.env` and add:
     ```
     GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
     ```

3. **Install Miniconda** (if you don’t have it)  
   Download and install from: https://docs.conda.io/en/latest/miniconda.html

4. **Create & activate environment**  
   ```bash
   conda env create -f environment.yml
   conda activate inbox_cleaner
   pip install -r requirements.txt
   ```

5. **Run the tool**  
   ```bash
   python inbox_cleaner.py
   ```
   - A browser window will open showing your summarized emails in styled cards.  
   - Enjoy!

---

## 3. Limitations

| What                    | Why                                   |
|-------------------------|---------------------------------------|
| Output Limit            | You can raise `max_results` in `'inbox_cleaner.py'` (1-500) per API call. |
| No Automatic Looping    | Script runs once and exits. You can add a cron job if you want repeat. |
| API quotas apply        | Gemini free tier is limited; watch your Google Cloud console for usage. |


---

## 4. Open Source & Contributions

This project is **100% open source** under the MIT License.  
Feel free to:

- Report bugs or request features  
- Fork the repo and submit pull requests  
- Improve docs, prompts, styling, or add new features  

Everyone’s welcome—let’s build together! 

by QAMBAR ABBAS

---

## 5. Credits

- **Project concept & design:** SHOZAB ABBAS (https://github.com/shozab-ctl)
- **Core implementation:** QAMBAR ABBAS
- **Inspired by:** Big MNCs need for lightweight, actionable inbox email management tools
