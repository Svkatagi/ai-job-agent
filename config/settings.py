# settings.py
# Configuration for AI-JOB-AGENT

import os
from dotenv import load_dotenv  # type: ignore

load_dotenv()

# Dynamic path resolution
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ChromeDriver path
CHROME_DRIVER_PATH = os.path.join(BASE_DIR, "tools", "driver", "chromedriver.exe")

# Resume and memory files
RESUME_TEXT_PATH = os.path.join(BASE_DIR, "memory", "resume.txt")
RESUME_PDF_PATH = os.path.join(BASE_DIR, "memory", "Resume Shreyas.Katagi.pdf")
FAQ_MEMORY_PATH = os.path.join(BASE_DIR, "memory", "faq_memory.json")

# Logs
LOG_PATH = os.path.join(BASE_DIR, "logs", "activity.log")
APPLICATION_LOG_PATH = os.path.join(BASE_DIR, "logs", "applications.csv")

# AI Model Config
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # Must be defined in .env
GEMINI_MODEL = "gemini-2.0-flash-exp"

# Relevance threshold for resume matching
RELEVANCE_THRESHOLD = 0.3

# Retry attempts for each job application
MAX_RETRIES = 3

# LinkedIn credentials
LINKEDIN_EMAIL = os.getenv("LINKEDIN_EMAIL")
LINKEDIN_PASSWORD = os.getenv("LINKEDIN_PASSWORD")

LINKEDIN_LOGIN_URL = "https://www.linkedin.com/login"
LINKEDIN_JOBS_URL = "https://www.linkedin.com/jobs/"
