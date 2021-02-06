import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class AddQuestionsTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get(' http://127.0.0.1:5000/sign_in')
        self.username = self.driver.find_element_by_id('l_username')
        self.password = self.driver.find_element_by_id('l_password')
        self.submit = self.driver.find_element_by_id('l_submit')

        self.username.send_keys('TestUser')
        self.password.send_keys('superhemligt')
        self.submit.send_keys(Keys.RETURN)
        self.driver.get('http://127.0.0.1:5000/add-question')


    def test_add_q(self):
        self.driver.find_element_by_class_name('category-select').click()
        select_cat = Select(self.driver.find_element_by_id('category'))
        select_cat.select_by_value('Sports')
        # select_asn = Select(self.driver.find_element_by_name('number'))
        # select_asn = Select(self.driver.find_elements_by_name('question'))
        # select_asn.deselect_all()
        # self.driver.find_element_by_id('submit').click()
        # self.assertIn('Lägg till', self.driver.page_source)
        time.sleep(5)



    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
