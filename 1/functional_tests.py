from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.brower=webdriver.Chrome()
        self.brower.implicitly_wait(3)
    def tearDown(self):
        self.brower.quit()

    def test_can_start_a_list(self):
        self.brower.get('http://localhost:8000')
        self.assertIn('To-Do',self.brower.title)
        self.fail('fintsh the test')
if __name__=='_main_':
        unittest.main(warnings='igore')