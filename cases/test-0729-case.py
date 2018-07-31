import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.chrome("https://www.zhihu.com/")
        print("测试开始")

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        self.driver.quit()
        print("测试结束")

    def test01(self):
        pass
