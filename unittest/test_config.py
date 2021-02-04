from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class WebTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')

    def login(self):
        self.driver.get('http://127.0.0.1:5000/sign_in')
        self.username = self.driver.find_element_by_id('l_username')
        self.password = self.driver.find_element_by_id('l_password')
        self.submit = self.driver.find_element_by_id('l_submit')
        self.username.send_keys('TestUser')
        self.password.send_keys('superhemligt')
        self.submit.send_keys(Keys.RETURN)

    def get_login_elements(self):
        self.driver.get('http://127.0.0.1:5000/sign_in')
        self.username = self.driver.find_element_by_id('l_username')
        self.password = self.driver.find_element_by_id('l_password')
        self.submit = self.driver.find_element_by_id('l_submit')

    def go_to(self, url):
        self.driver.get('http://127.0.0.1:5000'+url)

    def tearDown(self):
        self.driver.close()
