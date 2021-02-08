import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select



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

        self.question= self.driver.find_element_by_id('l_question')
        self.right_answer = self.driver.find_element_by_id('l_right_answer')
        self.wrong_answer1 = self.driver.find_element_by_id('l_wrong_answer1')
        self.wrong_answer2 = self.driver.find_element_by_id('l_wrong_answer2')
        self.wrong_answer3 = self.driver.find_element_by_id('l_wrong_answer3')
        self.submit =self.driver.find_element_by_id('submit')



    def test_add_q(self):
        self.driver.find_element_by_class_name('category-select').click()
        select_cat = Select(self.driver.find_element_by_id('category'))
        select_cat.select_by_value('General Knowledge')

        self.question.send_keys('What is the distance from the Earth to the sun?')
        self.right_answer.send_keys('150 million kilometers')
        self.wrong_answer1.send_keys('100 million kilometers')
        self.wrong_answer2.send_keys('200 million kilometers')
        self.wrong_answer3.send_keys('300 million kilometers')
        self.submit.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(3)
        self.assertIn('Frågan har blivit tillagd!', self.driver.page_source)



    def test_duplicates_add_q(self):
        self.driver.find_element_by_class_name('category-select').click()
        select_cat = Select(self.driver.find_element_by_id('category'))
        select_cat.select_by_value('General Knowledge')

        self.question.send_keys('What is the distance from the Earth to the sun?')
        self.right_answer.send_keys('150 million kilometers')
        self.wrong_answer1.send_keys('100 million kilometers')
        self.wrong_answer2.send_keys('200 million kilometers')
        self.wrong_answer3.send_keys('300 million kilometers')
        self.submit.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(3)
        self.assertIn('Din fråga är för lik en som redan existerar!', self.driver.page_source)



    def test_double_add_answers(self):
        self.driver.find_element_by_class_name('category-select').click()
        select_cat = Select(self.driver.find_element_by_id('category'))
        select_cat.select_by_value('General Knowledge')

        self.question.send_keys('Where is Lionel Messi from?')
        self.right_answer.send_keys('Rosario, Argentina')
        self.wrong_answer1.send_keys('Funchal, Portugal')
        self.wrong_answer2.send_keys('Mogi das Cruzes, State of São Paulo, Brazil')
        self.wrong_answer3.send_keys('Funchal, Portugal')
        self.submit.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(3)
        self.assertIn('Felaktiga svar måste vara unika!', self.driver.page_source)



    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
