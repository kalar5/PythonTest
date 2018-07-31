import unittest
from selenium import webdriver

# 继承了unittest.TestCase的一个类，会将除setUp和tearDown之外的所有方法看为一个测试用例


class TestCase(unittest.TestCase):
    # setUp和tearDown,则执行每个测试用例时，都会执行这两个方法
    # setUpClass和tearDownClass，则只会在该类执行时执行一次初始化和退出
    def setUp(self):
        # 用例执行之前初始化driver
        self.driver = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
        print("测试开始")

    def tearDown(self):
        # 关闭浏览器
        self.driver.quit()

    # @classmethod
    # def setUpClass(cls):
    #     # 用例执行之前初始化driver
    #     cls.driver = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
    #     print("测试开始")

    # @classmethod
    # def tearDownClass(cls):
    #     # 关闭打开的页面
    #     cls.driver.close()
    #     # 关闭浏览器
    #     cls.driver.exit()

    def test_01(self):
        self.driver.get("https://www.baidu.com")
        title = self.driver.title
        self.assertEqual(title, "百度一下，你就知道")