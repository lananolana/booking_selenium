"""
Authorization flow
"""
import pytest

from loguru import logger
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.login_page import Login
from utils.helpers import InputHelper
from utils.config import BASE_URL, ACCOUNT_URL, USERNAME, USERNAME_WITHOUT_AT_SIGN, PASSWORD

@pytest.fixture(scope = "module")
def common_classes(browser):
    """
    Classes for tests
    """
    login_page = Login(browser)
    base_page = BasePage(browser)
    input_helper = InputHelper(browser)

    return login_page, base_page, input_helper

def test_robot_auth(browser, common_classes):
    """
    Authorization with valid data and robot check
    """
    browser.get(BASE_URL)
    login_page, base_page, input_helper = common_classes

    login_page.login_click()
    base_page.find_clickable_element((By.ID, "username"))

    input_helper.enter_input(input_id = 'username', data = f"{USERNAME}")
    login_page.submit_button_click()

    base_page.check_url((f"{ACCOUNT_URL}sign-in/password"))
    input_helper.enter_input(input_id = 'password', data = f"{PASSWORD}")
    login_page.submit_button_click()

    login_page.click_and_hold((By.ID, "px-captcha"))

    alert = base_page.find_element((By.CSS_SELECTOR, '[class*="bui-spacer--medium"] h4'), 15)
    assert alert.text == "Having trouble?", "Unexpected result"

def test_no_email(browser, common_classes):
    """
    Authorization without email
    """
    browser.get(BASE_URL)

    login_page, base_page, _ = common_classes

    login_page.login_click()
    base_page.find_clickable_element((By.ID, "username"))
    login_page.submit_button_click()

    alert = base_page.find_element((By.ID, "username-note"))
    assert alert.text == "Enter your email address", "Unexpected username note"

def test_new_email(browser, common_classes):
    """
    Authorization with new email
    """
    browser.get(BASE_URL)

    login_page, base_page, input_helper = common_classes

    login_page.login_click()
    base_page.find_clickable_element((By.ID, "username"))
    input_helper.enter_input(input_id = 'username', data = f"new{USERNAME}")
    login_page.submit_button_click()

    base_page.check_url((f"{ACCOUNT_URL}register/password")) 
    page_header = base_page.find_element((By.CSS_SELECTOR, '[class="page-header"] h1'), 15)
    assert page_header.text == "Create password", "Unexpected page header"

    register_form = base_page.find_element((By.CLASS_NAME, "nw-register"))
    assert register_form, "No register form found"

def test_invalid_email(browser, common_classes):
    """
    Authorization with invalid email (without @)
    """
    browser.get(BASE_URL)

    login_page, base_page, input_helper = common_classes
    
    login_page.login_click()
    base_page.find_clickable_element((By.ID, "username"))
    input_helper.enter_input(input_id = 'username', data = f"{USERNAME_WITHOUT_AT_SIGN}")
    login_page.submit_button_click()

    alert = base_page.find_element((By.ID, "username-note"))
    assert alert.text == "Make sure the email address you entered is correct.", "Unexpected username note"