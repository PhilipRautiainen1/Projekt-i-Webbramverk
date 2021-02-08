from telnetlib import EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class RoutesTestCase(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('http://127.0.0.1:5000/sign_in')
        self.username = self.driver.find_element_by_id('l_username')
        self.password = self.driver.find_element_by_id('l_password')
        self.submit = self.driver.find_element_by_id('l_submit')

    def testLogOut(self):
        switch = False
        self.username.send_keys('TestUser')
        self.password.send_keys('superhemligt')
        self.submit.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(3)
        self.assertIn('Min sida', self.driver.page_source)
        self.log_out = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'sign-out')))
        self.log_out.click()
        if WebDriverWait(self.driver, 20).until(EC.url_changes):
            switch = True
        self.assertIs(switch, True)

    def testStartGameLoggedIn(self):
        switch = False
        new_url = 'http://127.0.0.1:5000/setup'
        self.username.send_keys('TestUser')
        self.password.send_keys('superhemligt')
        self.submit.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(3)
        self.assertIn('Min sida', self.driver.page_source)
        self.button = self.driver.find_element_by_xpath("//*[contains(text(), 'Singleplayer')]")
        self.button.click()
        if WebDriverWait(self.driver, 20).until(EC.url_matches(new_url)):
            switch = True
        self.assertIs(switch, True)

    def tearDown(self):
        self.driver.close()



