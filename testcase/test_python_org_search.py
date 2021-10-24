import unittest
from selenium import webdriver
from testcase import page


class PythonOrgSearchTest(unittest.TestCase):

    def setUp(self):
        print("setup")
        self.driver = webdriver.Chrome()
        self.driver.get('https://hejto.pl')

    def test_login_should_be_successful(self):
        # Arrange:
        log_in()
        # Act:
        click
        # Assert:
        assert click_result == True
        assert ctt == tst

        main_page = page.MainPage(self.driver)
        assert main_page.is_title_match()
        main_page.click_login_button()
        main_page.try_to_log_in("pan_tuman", "jestembotem")
        main_page.is_login_success()

    def tearDown(self):
        self.driver.close()