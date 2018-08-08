# import unittest
# from selenium import webdriver
# import time
# from common import open_url
# from common import find_element
# # from common import find_elements
# from common import send_keys
# from common import quit_driver


# class TestDemo(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.driver = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
#         print("测试开始")

#     @classmethod
#     def tearDownClass(cls):
#         # cls.driver.quit()
#         quit_driver(cls.driver)

#         print("测试结束")

#     # 常用操作
#     # 存在驱动问题
#     def test01(self):
#         self.driver.get("http://www.zhihu.com")
#         # 字符串中出现"需要进行转义(前面添加\)或者将其变为[']
#         search_input = self.driver.find_element_by_xpath("//*[@id='Popover1-toggle']")
#         search_input.send_keys("拼多多")
#         search_botton = self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/header/div/div[1]/div/form/div/div/div/div/button")
#         search_botton.click()
#         time.sleep(2)

#     # 简单的封装
#     def test02(self):
#         open_url("https://www.zhihu.com")
#         search_input1 = find_element(self.driver, 'xpath', "//*[@id='Popover1-toggle']")
#         send_keys(search_input1, "知乎")
#         search_botton1 = find_element(self.drive, 'xpath', "//*[@id='root']/div/div[2]/header/div/div[1]/div/form/div/div/div/div/button")
#         search_botton1.click()
#         time.sleep(2)
