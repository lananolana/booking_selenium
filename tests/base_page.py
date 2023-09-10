"""
POM base page
"""
from loguru import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config import BASE_URL, ACCOUNT_URL

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
    
    def find_elements(self, locator, time = 10):
        """
        Find elements with waiting
        """
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message = f"Can't find elements by locator {locator}")
    
    def go_to_site(self):
        """
        Get base URL
        """
        return self.driver.get(self.base_url)

    def go_to_sign_in(self):
        """
        Go to Sign in
        """
        logger.info('Find element')
        self.find_element(By.CLASS_NAME, 'data-testid="header-sign-in-button"').click()
        logger.info('Wait for page')
        WebDriverWait(self.driver, timeout = 5, poll_frequency = 1).until(EC.url_to_be(f"{ACCOUNT_URL}/sign-in"))