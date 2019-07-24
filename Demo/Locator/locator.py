
from selenium import webdriver


class Locator(object):

        def __init__(self, driver):
            self.driver = driver

        def findxpath(self, xpath):
            return self.driver.find_element_by_xpath(xpath)

        def sendkey(self, xpath, text):
            return self.findxpath(xpath).send_keys(text)

        def click(self, xpath):
            return self.findxpath(xpath).click()

        def gettitle(self):
            return self.driver.title
