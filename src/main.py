# src/main.py
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from tools.logger import init_logger
from tools.tracker import track_application
from tools.uploader import upload_resume_if_required
from src.observer import Observer
from agents.job_apply_agent import JobApplyAgent
from config.settings import get_settings
from dotenv import load_dotenv #type: ignore
import json

# Load environment variables (like Gemini API key)
load_dotenv()

# Initialize global settings
settings = get_settings()

# Set up logging
logger = init_logger()

# Load resume and FAQ memory once
with open("memory/resume.txt", "r", encoding="utf-8") as f:
    resume_text = f.read()

with open("memory/faq_memory.json", "r", encoding="utf-8") as f:
    faq_memory = json.load(f)

# Get the dynamic chromedriver
def get_chrome_driver():
    driver_path = os.path.join("tools", "driver", "chromedriver.exe")
    service = Service(executable_path=driver_path)
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def main():
    driver = get_chrome_driver()
    observer = Observer(driver, logger)
    agent = JobApplyAgent(driver, resume_text, faq_memory, observer, logger)

    logger.info("🤖 AI Job Agent started.")
    try:
        agent.run()
    except Exception as e:
        logger.error(f"Fatal error: {e}")
    finally:
        driver.quit()
        logger.info("✅ ChromeDriver closed, session complete.")

if __name__ == "__main__":
    main()
