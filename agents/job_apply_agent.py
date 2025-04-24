# agents/job_apply_agent.py

from src.job_parser import parse_job_card, extract_job_description
from src.form_filler import fill_form_fields
from tools.logger import log_step
from tools.tracker import log_application_result
from tools.uploader import upload_resume
import time
import json

class JobApplyAgent:
    def __init__(self, driver, resume_text, faq_memory, observer, logger):
        self.driver = driver
        self.resume_text = resume_text
        self.faq_memory = faq_memory
        self.observer = observer
        self.logger = logger
        self.success_count = 0
        self.failure_count = 0

    def run(self):
        job_cards = self.observer.get_job_cards()
        for idx, card in enumerate(job_cards):
            log_step(self.logger, f"📌 Opening job card {idx+1}/{len(job_cards)}")
            try:
                card.click()
                time.sleep(0.5)

                if not self.observer.open_easy_apply_modal():
                    continue

                job_title, company, jd_text = extract_job_description(self.driver)
                if not self.observer.is_relevant(job_title, jd_text, self.resume_text):
                    log_step(self.logger, f"⛔ Skipping irrelevant job: {job_title} @ {company}")
                    continue

                questions = self.observer.extract_questions()
                answers = self.observer.answer_questions(questions, jd_text, self.faq_memory, self.resume_text)

                fill_form_fields(self.driver, questions, answers)
                upload_resume(self.driver)

                submitted = self.observer.submit_application()
                log_application_result(company, job_title, submitted)
                if submitted:
                    self.success_count += 1
                else:
                    self.failure_count += 1

                self.observer.close_success_modal()

            except Exception as e:
                log_step(self.logger, f"❌ Failed on card {idx+1}: {str(e)}")
                self.failure_count += 1

        log_step(self.logger, f"✅ Done. Applied: {self.success_count}, Failed: {self.failure_count}")


def load_resume_memory(resume_path: str) -> str:
    """Load resume text from file."""
    with open(resume_path, "r", encoding="utf-8") as file:
        return file.read()

def load_faq_memory(faq_path: str) -> dict:
    """Load FAQ memory from JSON file."""
    with open(faq_path, "r", encoding="utf-8") as file:
        return json.load(file)

def is_job_relevant(job_description: str, resume_text: str, threshold: int = 30) -> bool:
    """Simple keyword relevance filter based on overlap between resume and job description."""
    job_words = set(job_description.lower().split())
    resume_words = set(resume_text.lower().split())
    overlap = job_words & resume_words
    relevance_score = len(overlap) / max(len(job_words), 1) * 100
    return relevance_score >= threshold