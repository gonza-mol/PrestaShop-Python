import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class AccountPageLocators:
    titleAccountPage = (By.CSS_SELECTOR, "#content>h2:nth-child(1)")



class AccountPage:

    def __init__(self, driver):
        self.driver = driver


    def showTitleAccountPage(self):
        return self.driver.find_element(*AccountPageLocators.titleAccountPage).text

