import unittest
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover('.', pattern='test_case_*.py')
    result = BeautifulReport(test_suite)
    result.report(filename='report_all.html', description='执行所有测试用例', log_path='report')