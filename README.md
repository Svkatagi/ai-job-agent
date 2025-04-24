# 🤖 AI-JOB-AGENT: Autonomous Job Application System

**AI-JOB-AGENT** is a fully **AI-controlled**, autonomous job application system powered by the **Gemini-2.0-Flash-Exp** model. It intelligently applies to LinkedIn Easy Apply jobs based on HTML DOM parsing, resume-based relevance checks, and long-term memory. This is not a bot—it’s an **intelligent agent** that observes, learns, adapts, and improves.

---

## 🚀 Features

- ✅ **HTML DOM Parsing** – Parses modal fields and form structures dynamically.
- ✅ **Relevance Filtering** – Applies only to jobs matching ≥30% with your resume.
- ✅ **Gemini Model Reasoning** – Answers questions using your resume and job description context.
- ✅ **FAQ Memory Reuse** – Uses `faq_memory.json` for basic recurring fields (email, phone, gender, etc.).
- ✅ **Resume Upload** – Attaches `Resume Shreyas.Katagi.pdf` automatically when required.
- ✅ **Navigation Handling** – Detects and clicks Next, Submit, Continue, or similar buttons.
- ✅ **Retry System** – Retries failed submissions up to 3 times; prompts user if all fail.
- ✅ **Success Detection** – Waits for confirmation modal before proceeding.
- ✅ **Action Logging** – Logs every action, decision, and message with timestamps.
- ✅ **Modular Tools** – Form filling, tracking, file uploading, parsing handled independently.

---

## 🧠 Agent Workflow

1. Load resume and FAQ memory once at startup.
2. Launch dynamic ChromeDriver and open LinkedIn.
3. Iterate through job cards and enter each modal.
4. Parse the HTML DOM and extract fields/questions.
5. Check job relevance using `resume.txt`.
6. Fill answers using FAQ or Gemini if necessary.
7. Upload PDF resume if required.
8. Click Submit/Next and wait for modal to close.
9. Record all prompts, answers, status, and time.
10. Retry failed attempts (up to 3x) before asking the user.
11. Move to the next job and repeat.

---

## 📁 Project Structure

```plaintext
AI-JOB-AGENT/
│
├── agents/
│   └── job_apply_agent.py            # Agent orchestration logic
│
├── config/
│   └── settings.py                   # Paths, delays, limits
│
├── logs/
│   └── activity.log                  # Full step-by-step log
│
├── memory/
│   ├── faq_memory.json               # Auto-filled FAQ responses
│   ├── resume.txt                    # Text-based parsed resume
│   └── Resume Shreyas.Katagi.pdf     # Resume to upload
│
├── src/
│   ├── main.py                       # Entry point
│   ├── form_filler.py                # Form field logic
│   ├── html_handler.py               # Parses HTML DOM
│   ├── job_parser.py                 # Relevance and job metadata
│   ├── observer.py                   # Browser DOM monitoring
│   └── browser.py                    # Launches and manages dynamic ChromeDriver
│
├── tools/
│   ├── logger.py                     # Timestamped logging
│   ├── tracker.py                    # Tracks job applications
│   ├── uploader.py                   # Handles file uploads
│   └── driver/
│       └── chromedriver.exe         # Dynamic driver path
│
├── .env                              # Gemini API key
├── .gitignore                        # Ignore venv, __pycache__, logs
├── README.md                         # Project documentation
└── requirements.txt                  # All dependencies
