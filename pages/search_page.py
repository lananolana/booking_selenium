"""
Search Page
"""
import time
from datetime import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.helpers import InputHelper

class SearchLocators:
    """
    Locators for search page
    """
    CITY_FIELD = (By.CSS_SELECTOR, '[data-testid="destination-container"]')
    SEARCHBOX_DATES = (By.CSS_SELECTOR, '[data-testid="searchbox-dates-container"]')
    START_DATE = (By.CSS_SELECTOR, '[data-testid="date-display-field-start"]')
    END_DATE = (By.CSS_SELECTOR, '[data-testid="date-display-field-end"]')

    GENIUS_POPUP = (By.CSS_SELECTOR, '[aria-label="Dismiss sign-in info."]')

    BREADCRUMBS = (By.CSS_SELECTOR, '[data-testid="breadcrumbs"]')
    PROPERTY_CARD = (By.CSS_SELECTOR, '[data-testid="property-card"]')
    ADDRESS = (By.CSS_SELECTOR, '[data-testid="address"]')

    CAROUSEL = (By.CSS_SELECTOR, '[data-testid="webcore-carousel-heading"]')

class Search(BasePage):
    """
    Class for search
    """
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
    
    def select_city(self, city):
        """
        Select destination
        """
        base_page = BasePage(self.browser)
        base_page.find_element(SearchLocators.CITY_FIELD)

        input_helper = InputHelper(self.browser)
        input_helper.enter_input(input_id = ":re:", data = city)

    def select_dates(self, check_in_date, check_out_date):
        """
        Select check in and check out dates
        """
        base_page = BasePage(self.browser)
        dates = base_page.find_element(SearchLocators.SEARCHBOX_DATES)
        dates.click()

        check_in = base_page.find_clickable_element((By.CSS_SELECTOR, f'[data-date="{check_in_date}"]'))
        check_in.click()

        check_out = base_page.find_element((By.CSS_SELECTOR, f'[data-date="{check_out_date}"]'))
        check_out.click()
    
    def check_breadcrumbs(self, city, time = 10):
        """
        Check city in breadcrumbs with waiting
        """
        return WebDriverWait(self.browser, time).until(
            EC.text_to_be_present_in_element(SearchLocators.BREADCRUMBS, city),
            message = f"Can't find city {city} in breadcrumbs")

    def check_address(self, city, time = 10):
        """
        Check city in property cards with waiting
        """
        base_page = BasePage(self.browser)
        property_cards = base_page.find_elements(SearchLocators.PROPERTY_CARD)

        for card in property_cards:
            return WebDriverWait(self.browser, time).until(
                EC.text_to_be_present_in_element(SearchLocators.ADDRESS, city),
                message = f"Can't find city {city} in property card")

    def check_start_date(self, date):
        """
        Check start date matches check-in date
        """
        base_page = BasePage(self.browser)
        start_date = base_page.find_element(SearchLocators.START_DATE)
        start_date_text = start_date.text

        check_in_date = datetime.strptime(date, '%Y-%m-%d')
        year = check_in_date.year

        start_date_object = datetime.strptime(start_date_text, '%a, %b %d')
        start_date_object_with_year = start_date_object.replace(year = year)

        return start_date_object_with_year.strftime('%Y-%m-%d')

    def check_end_date(self, date):
        """
        Check end date matches check-out date
        """
        base_page = BasePage(self.browser)
        end_date = base_page.find_element(SearchLocators.END_DATE)
        end_date_text = end_date.text

        check_out_date = datetime.strptime(date, '%Y-%m-%d')
        year = check_out_date.year

        end_date_object = datetime.strptime(end_date_text, '%a, %b %d')
        end_date_object_with_year = end_date_object.replace(year = year)

        return end_date_object_with_year.strftime('%Y-%m-%d')
    
    def check_carousel(self, city, time = 15):
        """
        Check carousel match selected city
        """
        driver = self.browser
        driver.execute_script("window.scrollBy(0, 1000);")

        return WebDriverWait(self.browser, time).until(
            EC.text_to_be_present_in_element(SearchLocators.CAROUSEL, city),
            message = f"Can't find city {city} in carousel heading")
    
    def close_popup(self):
        """
        Close Genius popup
        """
        base_page = BasePage(self.browser)
        close_button = base_page.find_element(SearchLocators.GENIUS_POPUP)
        close_button.click()