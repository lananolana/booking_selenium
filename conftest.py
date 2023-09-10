"""
Conftest file for project
"""
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope = "session")
def browser():
    """
    Basic fixture: Opening browser
    """
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized") # Open browser in maximized mode
    chrome_options.add_argument("--disable-infobars") # Disabling infobars
    chrome_options.add_argument("--disable-extensions") # Disabling extensions
    chrome_options.add_argument("--disable-dev-shm-usage") # Overcome limited resource problems
    chrome_options.add_argument("--headless") # Special mode "without browser"

    service = Service()
    driver = webdriver.Chrome(service = service, options = chrome_options)
    yield driver
    driver.quit()