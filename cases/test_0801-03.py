import unittest
import pyselenium


class testDemo1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = pyselenium.Pyselenium()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test01(self):
        self.driver.openurl("https://www.baidu.com")
        # self.driver.get_element("xpath-->//*[@id=\"kw\"]")
        self.driver.sendKeys("xpath-->//*[@id=\"kw\"]", "知乎")
        self.driver.click("id-->su")
        title = self.driver.get_title()
        self.assertEquals(title, "百度一下，你就知道")
