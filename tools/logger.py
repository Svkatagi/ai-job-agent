# tools/logger.py

import os
from datetime import datetime

def log(message: str):
    """Log a message with a timestamp to the console and a log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}"
    print(log_entry)

    with open("logs/activity.log", "a", encoding="utf-8") as log_file:
        log_file.write(log_entry + "\n")

LOG_FILE = "logs/ai_job_agent.log"

# Ensure the log directory exists
os.makedirs("logs", exist_ok=True)


def log_console(message: str) -> None:
    """
    Logs message to console and to log file with a timestamp.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted = f"[{timestamp}] {message}"
    print(formatted)

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(formatted + "\n")

def log_action(action: str):
    """
    Logs specific actions taken by the agent, used in job_parser and others.
    """
    log_console(f"📝 ACTION: {action}")

def log_step(step: str):
    """
    Logs a key workflow step with a timestamp.
    """
    log_console(f"[STEP] {step}")