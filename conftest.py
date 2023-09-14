"""
Conftest file for project
"""
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.base_page import BasePage
from pages.login_page import Login
from pages.search_page import Search
from utils.helpers import InputHelper

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
    # chrome_options.add_argument("--headless") # Special mode "without browser"

    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    chrome_options.add_argument(f"User-Agent={user_agent}")

    service = Service()
    driver = webdriver.Chrome(service = service, options = chrome_options)
    yield driver
    driver.quit()

@pytest.fixture(scope = "module")
def common_classes(browser):
    """
    Classes for tests
    """
    login_page = Login(browser)
    base_page = BasePage(browser)
    input_helper = InputHelper(browser)

    return {
        "login_page": login_page,
        "base_page": base_page,
        "input_helper": input_helper
    }