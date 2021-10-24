from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def go_to_main_site():
    driver.get("https://hejto.pl")


def accept_cookies():
    accept_cookies_button = driver.find_element(By.XPATH, '//*[contains(text(), "Zgadzam się")]')
    accept_cookies_button.click()


go_to_main_site()
driver.implicitly_wait(3)


try:
    accept_cookies()
except:
    print('There is no such thing as cookies...')
finally:
    driver.maximize_window()


# First part - testing login

_login = "pan_tuman"
_password = "jestembotem"


def log_in(login=None, password=None):
    login_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Zaloguj się"]')
    login_button.click()
    driver.implicitly_wait(1)
    login_input = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
    login_input.send_keys(login)
    password_input = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
    password_input.send_keys(password)
    let_me_in_button = driver.find_element(By.XPATH, '//button[text()="Zaloguj się"]')
    let_me_in_button.click()
    try:
        driver.find_element(By.ID, 'status')
        print("Login failed :(")
    except:
        print("Login success!")


log_in(_login, _password)

# Second part - check if any new notification

driver.implicitly_wait(3)


def check_notifications():
    try:
        driver.find_element(By.XPATH, '//div[@class="w-6 h-6 absolute -top-2 -right-1 rounded-full '
                                      'text-common-white bg-primary-main text-xs flex justify-center '
                                      'items-center"]')
        print("Yeah, you've got some notification!")
    except:
        print("There is no notifications at all :(")
        return

    notification_button_on = driver.find_element(By.CSS_SELECTOR, 'button[aria-expanded="false"]')
    notification_button_on.click()
    show_notification_list = driver.find_element(By.XPATH, '//a[text()="Pokaż pełną listę"]')
    show_notification_list.click()


check_notifications()
driver.implicitly_wait(2)

# Third part - testing search bar

go_to_main_site()
my_searched_data = "test"


def search_something(text=None):
    search_bar = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Szukaj"]')
    search_bar.send_keys(text, Keys.ENTER)
    try:
        driver.find_element(By.XPATH, '//span[text()="Brak wpisów"]')
        print(f"There is no any {text} here")
    except:
        print(f"Sir! We found {text}!")


search_something(my_searched_data)

driver.quit()
