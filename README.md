# 🤖 AI-JOB-AGENT: Autonomous Job Application Agent

AI-JOB-AGENT is a fully autonomous AI agent built using the Gemini-2.0-Flash-Exp model that intelligently applies to LinkedIn Easy Apply jobs. Unlike traditional bots, this agent observes the HTML DOM, interprets fields, learns from feedback, tracks errors, and applies only to relevant roles based on your resume and long-term memory.

---

## 🚀 Features

- ✅ **HTML DOM Observation** – Parses job application modals and forms live.
- ✅ **Relevance Filter** – Applies only if job relevance > 30%.
- ✅ **Gemini AI** – Answers application questions intelligently using resume.txt and job descriptions.
- ✅ **Autonomous Decision-Making** – Handles modals, clicks, errors, file uploads, and form navigation (Next/Submit).
- ✅ **Long-Term Memory** – Uses `faq_memory.json` and `resume.txt` to answer repetitive questions.
- ✅ **Retry Mechanism** – Retries failed applications up to 3 times before asking user input.
- ✅ **Logs Everything** – Tracks every click, action, and AI prompt-response with timestamps.
- ✅ **Modular** – Uses clean Python modules (`observer`, `form_filler`, `logger`, `tracker`, etc.).

---

## 🧠 Agent Flow (Workflow)

1. Load resume & FAQs into memory.
2. Start job card loop on LinkedIn Easy Apply.
3. Parse job HTML using `observer.py`.
4. Check job relevance using `resume.txt`.
5. Use Gemini model to answer form fields.
6. Upload resume if required.
7. Detect & click `Next`, `Submit`, or similar buttons.
8. Log application outcome (success/failure + reason).
9. Retry failed forms up to 3x, then prompt user.

---

## 📁 Project Structure

```plaintext
AI-JOB-AGENT/
│
├── agents/
│   └── job_apply_agent.py
│
├── config/
│   └── settings.py
│
├── logs/
│   └── activity.log
│
├── memory/
│   ├── faq_memory.json
│   └── resume.txt
│
├── src/
│   ├── main.py
│   ├── form_filler.py
│   ├── html_handler.py
│   ├── job_parser.py
│   └── observer.py
│
├── tools/
│   ├── logger.py
│   ├── tracker.py
│   └── uploader.py
│
├── .gitignore
├── README.md
└── requirements.txt


