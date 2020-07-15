from selenium.webdriver.support.ui import WebDriverWait


class BasePageElement(object):
    def __get__(self, instance, owner):
        driver = instance.driver
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element(*self.locator))
        element = driver.find_element(*self.locator)
        return element

    def __init__(self, locator):
        self.locator = locator


class ButtonElement(BasePageElement):
    def this_future_can_update(self):
        print("wait update!!!")


class InputElement(BasePageElement):
    def __set__(self, instance, value):
        self.__get__(instance, value).send_keys(value)
