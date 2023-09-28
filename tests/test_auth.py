"""
Authorization flow
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.login_page import Login
from utils.config import BASE_URL, USERNAME, USERNAME_WITHOUT_AT_SIGN, PASSWORD

def test_robot_auth(browser):
    """
    Authorization with valid data and robot check
    """
    login_page = Login(browser)
    base_page = BasePage(browser)

    browser.get(BASE_URL)
    login_page.login_click()

    login_page.enter_email(f"{USERNAME}")
    base_page.submit_button_click()

    login_page.enter_password(f"{PASSWORD}")
    base_page.submit_button_click()

    login_page.click_and_hold((By.ID, "px-captcha"))

    alert = base_page.find_element((By.CSS_SELECTOR, '[class*="bui-spacer--medium"] h4'), 15)
    assert alert.text == "Having trouble?", "Unexpected result"

def test_no_email(browser):
    """
    Authorization without email
    """
    login_page = Login(browser)
    base_page = BasePage(browser)

    browser.get(BASE_URL)
    login_page.login_click()

    base_page.find_clickable_element((By.ID, "username"))
    base_page.submit_button_click()

    alert = base_page.find_element((By.ID, "username-note"))
    assert alert.text == "Enter your email address", "Unexpected username note"

def test_new_email(browser):
    """
    Authorization with new email
    """
    login_page = Login(browser)
    base_page = BasePage(browser)

    browser.get(BASE_URL)
    login_page.login_click()

    login_page.enter_email(f"new{USERNAME}")
    base_page.submit_button_click()

    base_page.check_url(("password")) 
    page_header = base_page.find_element((By.CSS_SELECTOR, '[class="page-header"] h1'), 15)
    assert page_header.text == "Create password", "Unexpected page header"

    register_form = base_page.find_element((By.CLASS_NAME, "nw-register"))
    assert register_form, "No register form found"

def test_invalid_email(browser):
    """
    Authorization with invalid email (without @)
    """
    login_page = Login(browser)
    base_page = BasePage(browser)

    browser.get(BASE_URL)
    login_page.login_click()

    login_page.enter_email(f"{USERNAME_WITHOUT_AT_SIGN}")
    base_page.submit_button_click()

    alert = base_page.find_element((By.ID, "username-note"))
    assert alert.text == "Make sure the email address you entered is correct.", "Unexpected username note"