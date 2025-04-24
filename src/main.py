# main.py
# Entry point for AI-JOB-AGENT – fully autonomous LinkedIn Easy Apply system
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
from tools.logger import log
from tools.tracker import init_application_log
from tools.uploader import upload_resume_if_required
from tools.tracker import log_application_result
from src.observer import detect_easy_apply_jobs, observe_modal_fields
from src.job_parser import extract_job_description
from src.form_filler import fill_form_fields
from src.html_handler import handle_next_or_submit
from config.settings import (
    CHROME_DRIVER_PATH,
    MAX_RETRIES,
    RELEVANCE_THRESHOLD,
    RESUME_TEXT_PATH,
    FAQ_MEMORY_PATH
)
from agents.job_apply_agent import load_resume_memory, load_faq_memory, is_job_relevant
from src.browser import get_browser
from src.browser import login_to_linkedin, go_to_jobs_page

# Load resume and memory once at startup
resume_memory = load_resume_memory(RESUME_TEXT_PATH)
faq_memory = load_faq_memory(FAQ_MEMORY_PATH)


def main():
    driver = get_browser(CHROME_DRIVER_PATH)
    login_to_linkedin(driver)
    go_to_jobs_page(driver)
    job_cards = detect_easy_apply_jobs(driver)

    log(f"🎯 {len(job_cards)} Easy Apply jobs found.")
    for index, job_card in enumerate(job_cards):
        try:
            log(f"\n➡️ Processing job card {index + 1}/{len(job_cards)}...")
            job_card.click()
            time.sleep(2)

            job_description = extract_job_description(driver)
            if not is_job_relevant(job_description, resume_memory, RELEVANCE_THRESHOLD):
                log("❌ Skipping job: Not relevant based on resume.")
                continue

            fields = observe_modal_fields(driver)
            upload_resume_if_required(driver)

            fill_form_fields(fields, job_description, faq_memory, resume_memory)

            result, reason = handle_next_or_submit(driver)

            log_application_result(index, result, reason)

        except Exception as e:
            log(f"❌ Failed on job card {index + 1}: {str(e)}")
            log_application_result(index, "failure", str(e))

        time.sleep(0.5)

    driver.quit()
    log("✅ Finished job application loop.")


if __name__ == "__main__":
    main()
