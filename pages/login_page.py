"""
Login Page
"""
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage

class LoginLocators:
    """
    Locators for login page
    """
    LOGIN = (By.CSS_SELECTOR, '[data-testid*="header-sign-in-button"]')
    BUTTON = (By.CSS_SELECTOR, '[type*="submit"]')

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
    
    def submit_button_click(self):
        """
        Submit button click
        """
        submit_button = self.find_element(LoginLocators.BUTTON)
        submit_button.click()

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
        