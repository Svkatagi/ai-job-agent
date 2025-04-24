# tools/tracker.py

import os
import csv
from datetime import datetime
from tools.logger import log_console

APPLICATION_LOG_FILE = "logs/application_status.csv"

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

def init_application_log():
    """Initialize the CSV log file if not already present."""
    if not os.path.exists(APPLICATION_LOG_FILE):
        with open(APPLICATION_LOG_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Timestamp", "Company", "Role", "Status", "Notes"])
        log_console("📁 Application status log initialized.")


def log_application_result(company: str, role: str, status: str, notes: str = ""):
    """Log a job application result to the CSV file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(APPLICATION_LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, company, role, status, notes])
    log_console(f"📝 Logged application to {company} for {role} with status: {status}")
