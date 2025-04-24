# src/observer.py

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from tools.logger import log_console
from time import sleep

def detect_easy_apply_jobs(driver: WebDriver) -> list[WebElement]:
    """
    Detect all job cards with the 'Easy Apply' label.
    """
    try:
        sleep(1)  # simulate human reading delay
        job_cards = driver.find_elements(By.CLASS_NAME, "job-card-container")
        easy_apply_cards = [
            card for card in job_cards
            if "Easy Apply" in card.text
        ]
        log_console(f"🧾 Found {len(easy_apply_cards)} Easy Apply jobs.")
        return easy_apply_cards
    except Exception as e:
        log_console(f"❌ Error detecting Easy Apply jobs: {e}")
        return []

def observe_modal_fields(driver: WebDriver) -> list[WebElement]:
    """
    Return a list of all visible input, textarea, or select fields in the Easy Apply modal.
    """
    try:
        sleep(0.5)
        modal = driver.find_element(By.CLASS_NAME, "jobs-easy-apply-modal")
        input_fields = modal.find_elements(By.XPATH, ".//input | .//textarea | .//select")
        log_console(f"🧪 Found {len(input_fields)} fields inside the modal.")
        return input_fields
    except NoSuchElementException:
        log_console("❌ Modal not found.")
        return []
    except Exception as e:
        log_console(f"❌ Error observing modal fields: {e}")
        return []
