#coding=UTF-8
import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import HTMLTestReportCN

class TestCase_5itest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('http://www.5itest.cn/register')

    def test_login(self):
        self.driver.find_element_by_id('register_email').send_keys('')
        self.driver.find_element_by_id('register-btn').click()
        self.assertTrue(EC.title_contains('注册'))
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    test_suite  = unittest.TestSuite()
    test_suite .addTest(TestCase_5itest('test_login'))
    unittest.TextTestRunner().run(test_suite)
    