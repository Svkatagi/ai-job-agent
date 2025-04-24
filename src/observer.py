# observer.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from tools.logger import log
import time

def detect_modal(driver):
    try:
        modal = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "jobs-easy-apply-modal"))
        )
        log("🧾 Easy Apply modal detected.")
        return modal
    except TimeoutException:
        log("❌ Modal not found.")
        return None

def detect_form_fields(modal):
    try:
        fields = modal.find_elements(By.CSS_SELECTOR, "input, textarea, select")
        log(f"🧪 Found {len(fields)} form fields.")
        return fields
    except Exception as e:
        log(f"❌ Failed to detect form fields: {e}")
        return []

def detect_next_button(driver):
    try:
        return driver.find_element(By.CSS_SELECTOR, "button[aria-label='Continue to next step']")
    except NoSuchElementException:
        return None

def detect_review_button(driver):
    try:
        return driver.find_element(By.CSS_SELECTOR, "button[aria-label='Review your application']")
    except NoSuchElementException:
        return None

def detect_submit_button(driver):
    try:
        return driver.find_element(By.CSS_SELECTOR, "button[aria-label='Submit application']")
    except NoSuchElementException:
        return None

def detect_success_modal(driver):
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'application was sent')]"))
        )
        log("✅ Application success modal detected.")
        return True
    except TimeoutException:
        log("⚠️ No success modal detected.")
        return False
