from locator import *
from element import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    # element on MainPage:
    button_go = ButtonElement(BaseLocator.GO_BUTTON)
    text_search = InputElement(BaseLocator.TEXT_SEARCH)

    def is_title_matches(self):
        return "Python" in self.driver.title

    def click_button_go(self):
        self.button_go.click()


class SearchResultPage(BasePage):
    def is_result_found(self):
        print(self.driver.page_source)
        return "No results found." not in self.driver.page_source
