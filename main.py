import unittest
from selenium import webdriver
import page


class PythonSearchOrg(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("https://www.python.org/")

    def test_search_on_page(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.text_search = "assgr3egfgb"
        mainPage.click_button_go()
        result_page_search = page.SearchResultPage(self.driver)
        assert result_page_search.is_result_found()

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
