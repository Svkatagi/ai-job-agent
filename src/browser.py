# src/browser.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config.settings import CHROME_DRIVER_PATH, LINKEDIN_EMAIL, LINKEDIN_PASSWORD, LINKEDIN_LOGIN_URL


def init_browser() -> webdriver.Chrome:
    """
    Initializes a Chrome browser using the local chromedriver in tools/driver.

    Returns:
        webdriver.Chrome: Chrome WebDriver instance with custom options.
    """
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    driver_path = os.path.join("tools", "driver", "chromedriver.exe")
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    return driver


def get_browser(chromedriver_path: str) -> webdriver.Chrome:
    """Launches Chrome with the provided driver."""
    service = Service(executable_path=chromedriver_path)
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(service=service, options=options)

def login_to_linkedin(driver):
    """Log in to LinkedIn using provided credentials."""
    driver.get(LINKEDIN_LOGIN_URL)
    time.sleep(2)

    email_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    email_input.send_keys(LINKEDIN_EMAIL)
    password_input.send_keys(LINKEDIN_PASSWORD)
    password_input.send_keys(Keys.RETURN)

    time.sleep(2)

def go_to_jobs_page(driver):
    """Navigate to LinkedIn Jobs page after login."""
    driver.get("https://www.linkedin.com/jobs/")
    time.sleep(3)