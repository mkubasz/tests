from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[aria-label="Zaloguj się"]')
    LOGIN_INPUT = (By.CSS_SELECTOR, 'input[name="username"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[name="password"]')
    LOG_IN_BUTTON = (By.XPATH, '//button[text()="Zaloguj się"]')
    LOGIN_STATUS = (By.ID, 'status')


class SearchResultsFromLocators(object):
    pass