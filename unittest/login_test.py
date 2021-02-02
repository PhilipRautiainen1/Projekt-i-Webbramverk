from unittest import TestCase
from selenium import webdriver


class LogInTests(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')

    def test_correct_login(self):
        pass

    def test_wrong_password_login(self):
        pass

    def test_wrong_username_login(self):
        pass

    def test_wrong_username_and_password_login(self):
        pass

    def tearDown(self):
        self.driver.close()
