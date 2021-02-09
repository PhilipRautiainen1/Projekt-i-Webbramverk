from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from view import app


class SetupTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('http://127.0.0.1:5000/sign_in')
        self.username = self.driver.find_element_by_id('l_username')
        self.password = self.driver.find_element_by_id('l_password')
        self.submit = self.driver.find_element_by_id('l_submit')
        self.username.send_keys('TestUser')
        self.password.send_keys('superhemligt')
        self.submit.send_keys(Keys.RETURN)
        self.driver.get('http://127.0.0.1:5000/setup')

    def test_setup(self):
        self.driver.find_element_by_id('category-selector').click()
        select_cat = Select(self.driver.find_element_by_name('category'))
        select_cat.select_by_value('Random')
        select_num = Select(self.driver.find_element_by_name('number'))
        select_num.select_by_value('3')
        self.driver.find_element_by_id('submit-setup').click()
        self.assertIn('Nästa fråga', self.driver.page_source)

    def tearDown(self):
        self.driver.close()
