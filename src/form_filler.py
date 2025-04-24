# src/form_filler.py

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from tools.logger import log_action
import time


def fill_fields(driver: WebDriver, fields: list[dict], answers: dict) -> None:
    """
    Fills input/select/textarea fields with AI-generated answers.
    """
    for field in fields:
        label = field["label"]
        field_id = field["id"]
        field_type = field["type"]
        answer = answers.get(label.strip())

        if not answer:
            log_action(f"⚠️ No answer found for field: {label}")
            continue

        try:
            element = driver.find_element(By.ID, field_id)

            if field_type == "input":
                element.clear()
                element.send_keys(answer)

            elif field_type == "textarea":
                element.clear()
                element.send_keys(answer)

            elif field_type == "select":
                # Choose first match (customize if dropdowns vary)
                for option in element.find_elements(By.TAG_NAME, "option"):
                    if answer.lower() in option.text.lower():
                        option.click()
                        break

            log_action(f"✅ Filled field '{label}' with '{answer}'")
            time.sleep(0.5)  # simulate human pause

        except (NoSuchElementException, ElementNotInteractableException) as e:
            log_action(f"❌ Failed to fill field '{label}': {e}")



def fill_form_fields(driver: WebDriver, answers: dict) -> None:
    """
    Fills out the Easy Apply form fields using the answers provided.
    Each key in `answers` is the field label, and value is the generated answer.
    """
    log_action("🖋️ Filling form fields...")
    try:
        for label, answer in answers.items():
            input_elements = driver.find_elements_by_xpath(f"//label[contains(., '{label}')]/following-sibling::input | //label[contains(., '{label}')]/following-sibling::textarea")
            if not input_elements:
                log_action(f"⚠️ No input element found for label: {label}")
                continue

            for element in input_elements:
                element.clear()
                element.send_keys(answer)
                time.sleep(0.2)  # Small delay to mimic human input

            log_action(f"✅ Filled: {label}")
    except Exception as e:
        log_action(f"❌ Error filling form fields: {e}")