"""
POM base page
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.config import BASE_URL

class BaseLocators:
    """
    Locators for base page
    """
    BUTTON = (By.CSS_SELECTOR, '[type*="submit"]')
    DECLINE_COOKIES_BUTTON = (By.ID, "onetrust-reject-all-handler")

class BasePage:
    """
    Base page
    """
    def __init__(self, driver):
        self.driver = driver
        self.base_url = BASE_URL

    def find_element(self, locator, time = 10):
        """
        Find element with waiting
        """
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message = f"Can't find element by locator {locator}")
    
    def find_clickable_element(self, locator, time = 10):
        """
        Find clickable and visible element with waiting
        """
        element = WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator),
                                                      message = f"Can't find visible element by locator {locator}")
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(element),
                                                      message = f"Can't find clickable element by locator {locator}")
    
    def find_elements(self, locator, time = 10):
        """
        Find elements with waiting
        """
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message = f"Can't find elements by locator {locator}")

    def check_url(self, locator, time = 10):
        """
        Check URL with waiting
        """
        return WebDriverWait(self.driver, time).until(EC.url_contains(locator),
                                                      message = f"URL doesn't contain {locator}")
    
    def submit_button_click(self):
        """
        Submit button click
        """
        submit_button = self.find_element(BaseLocators.BUTTON)
        submit_button.click()
    
    def decline_cookies(self):
        """
        Decline cookies
        """
        decline_button = self.find_element(BaseLocators.DECLINE_COOKIES_BUTTON)
        decline_button.click()