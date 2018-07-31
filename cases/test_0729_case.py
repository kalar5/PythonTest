import unittest
from selenium import webdriver


class TestDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
        print("测试开始")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("测试结束")

    def test01(self):
        pass
