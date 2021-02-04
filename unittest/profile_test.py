from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Data_mongo.repositories.user_repository import remove_friend, get_user
from view import app


class LogInTests(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('http://127.0.0.1:5000/sign_in')
        self.username = self.driver.find_element_by_id('l_username')
        self.password = self.driver.find_element_by_id('l_password')
        self.submit = self.driver.find_element_by_id('l_submit')
        self.username.send_keys('TestUser')
        self.password.send_keys('superhemligt')
        self.submit.send_keys(Keys.RETURN)
        self.driver.get('http://127.0.0.1:5000/profile')

    def test_correct_user(self):
        self.assertIn('TestUser', self.driver.page_source)

    def test_correct_friend_amount(self):
        with app.app_context():
            user = get_user('TestUser')
            correct_friend_amount = len(user.friends)
        friend_amount = len(self.driver.find_elements_by_class_name('friend_box'))
        self.assertEqual(correct_friend_amount, friend_amount)

    def test_add_friend(self):
        with app.app_context():
            user = get_user('TestUser')
            before_amount = len(user.friends)

        self.driver.find_element_by_id('add_button').click()
        friend = self.driver.find_element_by_name('friend_name')
        friend.send_keys('red93')
        self.driver.find_element_by_id('search_user').click()

        with app.app_context():
            user = get_user('TestUser')
            after_amount = len(user.friends)

        self.assertEqual(before_amount+1, after_amount)
        remove_friend(user, '600567849f70119672d65105')

    def tearDown(self):
        self.driver.close()
