import unittest
from selenium import webdriver
from testcase import page


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        print("setup")
        self.driver = webdriver.Chrome()
        self.driver.get("https://hejto.pl")

    def test_login(self):
        main_page = page.MainPage(self.driver)
        print("main page")
        assert main_page.is_title_matches()
        main_page.click_login_button()
        main_page.try_to_log_in("pan_tuman", "jestembotem")
        main_page.is_login_success()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
