# Date: 2019-7-24
# Author: Qin

from selenium import webdriver
import logging


class Driver(object):

        def __init__(self, driver):
            self.driver = driver

        def chromedriver(self):
            try:
                self.driver = webdriver.chrome()
            except Exception:
                logging.log("info", "The driver doesn't work")

        def firefoxdriver(self):
            try:
                self.driver = webdriver.firefox()
            except Exception:
                logging.log("info", "The driver doesn't work")

        def iedriver(self):
            try:
                self.driver = webdriver.ie()
            except Exception:
                logging.log("info", "The driver doesn't work")

        def get(self, url):
            self.driver.get(url)

        def quit(self):
            self.driver.quit()
