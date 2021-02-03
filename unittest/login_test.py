from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class LogInTests(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('http://127.0.0.1:5000/sign_in')
        self.username = self.driver.find_element_by_id('l_username')
        self.password = self.driver.find_element_by_id('l_password')
        self.submit = self.driver.find_element_by_id('l_submit')

    def test_correct_login(self):
        self.username.send_keys('TestUser')
        self.password.send_keys('superhemligt')
        self.submit.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(3)
        self.assertIn('Min sida', self.driver.page_source)

    def test_wrong_password_login(self):
        self.username.send_keys('TestUser')
        self.password.send_keys('superhemlis')
        self.submit.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(3)
        self.assertIn('Felaktigt användarnamn eller lösenord', self.driver.page_source)

    def test_wrong_username_login(self):
        self.username.send_keys('TestTest')
        self.password.send_keys('superhemligt')
        self.submit.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(3)
        self.assertIn('Felaktigt användarnamn eller lösenord', self.driver.page_source)

    def test_wrong_username_and_password_login(self):
        self.username.send_keys('TestTest')
        self.password.send_keys('superhemlis')
        self.submit.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(3)
        self.assertIn('Felaktigt användarnamn eller lösenord', self.driver.page_source)

    def tearDown(self):
        self.driver.close()
