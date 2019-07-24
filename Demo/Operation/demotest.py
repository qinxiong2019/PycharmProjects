from selenium import webdriver
from Demo.Locator.locator import Locator
import json
import logging

CONFIGURATION_JSON = "Demo/Locator/LocatorMap/locatormap.json"

# Load configuration
locatormap = json.load(open(CONFIGURATION_JSON))


class Operations(object):

    def login(self, username, password, url):
        title = ""

        try:
            self.driver = webdriver.Chrome()
            self.driver.get(url)
            op = Locator(self.driver)
            op.sendkey(locatormap["username_xpath"], username)
            op.sendkey(locatormap["password_xpath"], password)
            op.click(locatormap["loginbutton_xpath"])
            title = op.gettitle()
        except Exception:
            logging.log(1, "login failed")
        finally:
            self.quit()
        return title

    def quit(self):
        self.driver.quit()
