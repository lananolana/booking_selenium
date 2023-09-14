"""
Search flow
"""
from pages.search_page import Search
from pages.base_page import BasePage
from utils.config import BASE_URL, CITY, CHECK_IN, CHECK_OUT

def test_basic_search(browser):
    """
    Search hotels by city and dates
    """
    browser.get(BASE_URL)
    search_page = Search(browser)

    base_page = BasePage(browser)
    base_page.decline_cookies()

    search_page.select_city(CITY)
    search_page.select_dates(CHECK_IN, CHECK_OUT)

    base_page.submit_button_click()
    search_page.close_popup()

    assert search_page.check_breadcrumbs(CITY), f"There is no {CITY} in breadcrumbs"
    assert search_page.check_address(CITY), f"There is no {CITY} in one of the property cards"
    assert search_page.check_start_date(CHECK_IN) == CHECK_IN, f"Start date doesn't match the check-in date {CHECK_IN}"
    assert search_page.check_end_date(CHECK_OUT) == CHECK_OUT, f"End date doesn't match the check-out date {CHECK_OUT}"
    assert search_page.check_carousel(CITY), f"Carousel doesn't match selected {CITY}"
