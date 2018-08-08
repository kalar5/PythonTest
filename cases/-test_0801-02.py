from selenium import webdriver
import unittest
from until import readExcel


class testDemo1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("./driver/chromedriver.exe")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test01(self):
        self.driver.get("https://www.zhihu.com")
        data = readExcel.getTestdata(0, 0)
        search = self.driver.find_element_by_xpath("//*[@id=\"Popover1-toggle\"]")
        search.send_keys(data)
        searchClink = self.driver.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/header/div/div[1]/div/form/div/div/div/div/button")
        searchClink.click()
        title = self.driver.title
        self.assertIn(data, title)

    def test02(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_xpath("//*[@id=\"u1\"]/a[1]")
        title = self.driver.title
        self.assertEqual("百度新闻", title)

