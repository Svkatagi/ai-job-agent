# src/html_handler.py

from bs4 import BeautifulSoup # type: ignore
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

def handle_next_or_submit(driver: WebDriver) -> str:
    """
    Handles navigation in the Easy Apply modal by detecting and clicking 'Next', 'Continue', or 'Submit'.
    Returns which action was taken: 'next', 'submit', or 'none'.
    """
    buttons = ["Next", "Continue", "Submit application", "Review", "Submit"]
    for btn_text in buttons:
        try:
            button = driver.find_element(By.XPATH, f"//button[contains(., '{btn_text}')]")
            if button.is_displayed() and button.is_enabled():
                button.click()
                time.sleep(0.5)
                return btn_text.lower()
        except (NoSuchElementException, ElementClickInterceptedException):
            continue
    return "none"


def extract_form_fields(html: str) -> list[dict]:
    '''
    Parses the LinkedIn Easy Apply modal HTML and extracts all form fields.
    Returns a list of dictionaries with field 'label', 'type', and 'id'.
    '''
    soup = BeautifulSoup(html, "html.parser")
    fields = []

    for label in soup.find_all("label"):
        label_text = label.get_text(strip=True)
        input_element = label.find_next(["input", "textarea", "select"])

        if input_element:
            field_type = input_element.name
            field_id = input_element.get("id", "unknown")
            fields.append({
                "label": label_text,
                "type": field_type,
                "id": field_id
            })

    return fields
