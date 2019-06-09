#coding=UTF-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
'''
Python3的安装路径：
/Library/Frameworks/Python.framework/Versions/3.7/bin/
'''

def run():
    driver = webdriver.Chrome()
    driver.get('http://www.5itest.cn/register')
    sleep(3)
    EC.title_contains('注册了')

    driver.quit()


if __name__ == '__main__':
    run()


