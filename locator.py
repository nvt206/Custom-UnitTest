from selenium.webdriver.common.by import By


class BaseLocator(object):
    GO_BUTTON = (By.ID, "submit")
    TEXT_SEARCH = (By.ID, "id-search-field")
