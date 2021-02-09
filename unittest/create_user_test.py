from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from controllers.user_controller import get_user, delete_user


class SignUpTests(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('http://127.0.0.1:5000/signup')
        self.email = self.driver.find_element_by_id('email')
        self.username = self.driver.find_element_by_id('username')
        self.pass1 = self.driver.find_element_by_id('password1')
        self.pass2 = self.driver.find_element_by_id('password2')

    def test_signUp(self):
        self.email.send_keys('anders@email.com')
        self.username.send_keys('anders')
        self.pass1.send_keys('anders123')
        self.pass2.send_keys('anders123')
        self.pass2.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(5)
        self.assertIn('Logga in', self.driver.page_source)
        user = get_user('anders')
        self.assertEqual('anders', user.username)
        delete_user(user)



    def test_wrongUsernameSignUp(self):

        self.email.send_keys('anders@email.com')
        self.username.send_keys('a')
        self.pass1.send_keys('anders123')
        self.pass2.send_keys('anders123')
        self.pass2.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(5)
        self.assertIn('Användarnamnet måste vara minst 4 tecken långt.', self.driver.page_source)

    def test_wrongEmailSignUp(self):

        self.email.send_keys('andersemail.com')
        self.username.send_keys('anders')
        self.pass1.send_keys('anders123')
        self.pass2.send_keys('anders123')
        self.pass2.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(5)
        self.assertIn('Ange email i formatet namn@email.se', self.driver.page_source)

    def test_wrongPassMatchSignUp(self):

        self.email.send_keys('anders@email.com')
        self.username.send_keys('anders')
        self.pass1.send_keys('anders123')
        self.pass2.send_keys('anders23')
        self.pass2.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(5)
        self.assertIn('Lösenorden machar inte.', self.driver.page_source)

    def test_wrongPassFormatSignUp(self):

        self.email.send_keys('anders@email.com')
        self.username.send_keys('anders')
        self.pass1.send_keys('anders')
        self.pass2.send_keys('anders')
        self.pass2.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(5)
        self.assertIn('Lösenordet ska vara minst 8 tecken långt.', self.driver.page_source)