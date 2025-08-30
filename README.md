# 📰 AI News Summarizer

An AI-powered news aggregator that fetches the latest headlines, summarizes them into short and easy-to-read snippets, saves your reading history, and even reads news aloud with **Text-to-Speech (TTS)** or sends you a **daily email digest**.

Built with **Python**, **Streamlit**, and **NLP**.

---

## 🚀 Features

- 🔎 Fetch real-time news from **NewsAPI**
- ✨ Summarize articles using **NLP**
- 📜 Save & view reading history in SQLite
- 🔊 Listen to summaries via **Text-to-Speech (gTTS)**
- 📧 Get a daily email digest of top headlines
- 🌐 Clean UI built with **Streamlit**

---

## 📂 Project Structure

news-ai/
│── app.py # Main Streamlit app
│── news_api.py # Fetch news from NewsAPI
│── nlp.py # Summarization logic
│── db.py # SQLite database for history
│── tts.py # Text-to-Speech (gTTS)
│── email_digest.py # Daily email digest
│── requirements.txt # Project dependencies
│── .env # API keys and secrets
│── README.md # Project documentation

---

## ⚡ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/news-ai.git
cd news-ai

2. Create Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate

Mac/Linux
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Add API Keys
Create a .env file in the root folder:

NEWSAPI_KEY=your_newsapi_key_here
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_email_password_or_app_password

5. Run the App
streamlit run app.py
👉 Open http://localhost:8501 in your browser.

📦 Requirements
Python 3.8+
Streamlit
Requests
Sumy
gTTS
python-dotenv

Install with:
pip install -r requirements.txt


🎯 Future Improvements
🌙 Dark mode UI
📱 Mobile-friendly interface
🧠 Advanced summarizer (transformers like BART or T5)
🔔 Push notifications
```
