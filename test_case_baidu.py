import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from BeautifulReport import BeautifulReport
from time import sleep


class TestCaseBaidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('开始百度测试套件运行')
        cls.driver = webdriver.Chrome()

    def test_Open_WebSite(self):
        self.url = "http://www.baidu.com"
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.assertTrue(EC.title_contains('百度'))

    def test_Search(self):
        self.driver.find_element_by_name('wd').send_keys('Java')
        self.driver.find_element_by_id('su').click()
        key_word = self.driver.find_element_by_id('kw').get_attribute('value')
        self.assertEqual(key_word, 'Python')


    @classmethod
    def tearDownClass(cls):
        print('结束百度测试套件运行')
        sleep(3)
        cls.driver.quit()

if __name__ == '__main__':
    # test_suite = unittest.defaultTestLoader.discover('.',pattern='test_*.py')
    # result = BeautifulReport(test_suite)
    # result.report(filename='测试报告', description='第一次生成测试报告', log_path='report')
    test_suite = unittest.defaultTestLoader.discover('.',pattern='test_case_baidu.py')
    result = BeautifulReport(test_suite)
    result.report(filename='baidu.html',description='百度首页测试',log_path='report')
