"""
Login Page
"""
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from utils.helpers import InputHelper
from utils.config import ACCOUNT_URL

class LoginLocators:
    """
    Locator for login page
    """
    LOGIN = (By.CSS_SELECTOR, '[data-testid*="header-sign-in-button"]')

class Login(BasePage):
    """
    Class for login
    """
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def login_click(self):
        """
        Login button click
        """
        login_button = self.find_element(LoginLocators.LOGIN)
        login_button.click()

    def click_and_hold(self, locator):
        """
        Button click and hold
        """
        button = self.find_clickable_element(locator)

        actions = ActionChains(self.browser)
        actions.click_and_hold(button).perform()
        time.sleep(8)
        actions.release().perform()
        time.sleep(5)
    
    def enter_email(self, email):
        base_page = BasePage(self.browser)
        base_page.find_clickable_element((By.ID, "username"))
        
        input_helper = InputHelper(self.browser)
        input_helper.enter_input(input_id = 'username', data = email)
    
    def enter_password(self, password):
        base_page = BasePage(self.browser)
        base_page.check_url(("password"))
        base_page.find_clickable_element((By.ID, "password"))
        
        input_helper = InputHelper(self.browser)
        input_helper.enter_input(input_id = 'password', data = password)