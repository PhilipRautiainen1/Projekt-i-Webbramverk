from unittest import TestCase
from selenium import webdriver


class ErrorHandlersTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')

    def test_404(self):
        self.driver.get('http://127.0.0.1:5000/min-sida')
        self.assertIn('ERROR', self.driver.page_source)

    def tearDown(self):
        self.driver.close()
