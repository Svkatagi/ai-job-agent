# tools/uploader.py

import os
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from tools.logger import log_console

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
import os

def upload_resume(driver: WebDriver, input_element: WebElement) -> bool:
    """
    Uploads the resume file using the detected input element.
    Returns True if successful, False otherwise.
    """
    try:
        resume_path = os.path.join("memory", "Resume Shreyas.Katagi.pdf")
        input_element.send_keys(os.path.abspath(resume_path))
        return True
    except Exception as e:
        print(f"❌ Failed to upload resume: {e}")
        return False

def upload_resume_if_required(driver: WebDriver) -> bool:
    """
    Detects resume upload field and uploads resume from memory folder.
    Returns True if upload happened, else False.
    """
    resume_path = os.path.abspath("memory/Resume Shreyas.Katagi.pdf")

    try:
        upload_inputs = driver.find_elements(By.XPATH, "//input[@type='file']")
        for input_field in upload_inputs:
            label_element = input_field.find_element(By.XPATH, "./ancestor::div[contains(@class, 'jobs-easy-apply-form-section__grouping')]")
            if "resume" in label_element.text.lower():
                input_field.send_keys(resume_path)
                log_console("📎 Resume uploaded successfully.")
                return True
        return False
    except NoSuchElementException:
        log_console("⚠️ No resume upload field found.")
        return False
    except Exception as e:
        log_console(f"❌ Error while trying to upload resume: {e}")
        return False
