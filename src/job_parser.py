# src/job_parser.py

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from tools.logger import log

def parse_job_card(job_card: WebElement) -> dict:
    try:
        title = job_card.find_element(By.CLASS_NAME, "job-card-list__title").text.strip()
        company = job_card.find_element(By.CLASS_NAME, "job-card-container__company-name").text.strip()
        return {"title": title, "company": company}
    except Exception as e:
        log(f"❌ Error parsing job card: {e}")
        return {"title": "", "company": ""}

def extract_job_description(driver) -> str:
    try:
        job_desc_el = driver.find_element(By.CLASS_NAME, "jobs-description-content__text")
        return job_desc_el.text.strip()
    except Exception as e:
        log(f"❌ Error extracting job description: {e}")
        return ""
