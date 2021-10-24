from testcase.locator import *
from logger import logger
class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    def is_title_match(self):
        return "Hejto" in self.driver.title

    def click_login_button(self):
        element = self.driver.find_element(*MainPageLocators.LOGIN_BUTTON)
        element.click()

    def log_in(self, login=None, password=None):
        login_input = self.driver.find_element(*MainPageLocators.LOGIN_INPUT)
        login_input.send_keys(login)
        password_input = self.driver.find_element(*MainPageLocators.PASSWORD_INPUT)
        password_input.send_keys(password)
        log_in_button = self.driver.find_element(*MainPageLocators.LOG_IN_BUTTON)
        log_in_button.click()

    def is_login_success(self):
        try:
            self.driver.implicitly_wait(3)
            self.driver.find_element(*MainPageLocators.LOGIN_STATUS)
            return True
        except:
            logger.error('Login failed')
            return False
