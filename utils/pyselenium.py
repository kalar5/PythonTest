from selenium import webdriver


# python对selenium的get/getElement/getElements/sendKeys/clink/gitTitle/quit等方法进行二次封装
class pyselenium():
    def __init__(self, browser="Chrome"):
        if(browser == "Chrome"):
            driver = webdriver.Chrome("./driver/chromedriver.exe")

        elif(browser == "edge"):
            driver = webdriver.Edge()

        elif(browser == "fireFox"):
            driver = webdriver.Firefox()

        elif(browser == "Safari"):
            driver = webdriver.Safari()

        else:
            print("浏览器错误，请确认")
            raise

        self.driver = driver

    def maxWindow(self):
        self.driver.maximize_window()

    def openURL(self, url):
        self.driver.get(url)

    def getElement(self, byValue):
        by = byValue.splite("-->")[0]
        value = byValue.splite("-->")[1]

        if(by == "id"):
            element = self.driver.find_element_by_id(value)
        elif(by == "xpath"):
            element = self.driver.find_element_by_xpath(value)
        elif(by == "classname"):
            element = self.driver.find_element_by_class_name(value)
        elif(by == "tagname"):
            element = self.driver.find_element_by_tag_name(value)
        elif(by == "css"):
            element = self.driver.find_element_by_css_selector(value)
        elif(by == "link_text"):
            element = self.driver.find_element_by_link_text(value)
        else:
            print("没有这种寻找方式")
            raise
        return element

    def getElements(self, byValue):
            by = byValue.splite("-->")[0]
            value = byValue.splite("-->")[1]

            if(by == "id"):
                elements = self.driver.find_elements_by_id(value)
            elif(by == "xpath"):
                elements = self.driver.find_elements_by_xpath(value)
            elif(by == "classname"):
                elements = self.driver.find_elements_by_class_name(value)
            elif(by == "tagname"):
                elements = self.driver.find_elements_by_tag_name(value)
            elif(by == "css"):
                elements = self.driver.find_elements_by_css_selector(value)
            elif(by == "link_text"):
                elements = self.driver.find_elements_by_link_text(value)
            else:
                print("没有这种寻找方式")
                raise
            return elements

    def sendKeys(self, byValue, keys):
            element = self.getElement(byValue)
            element.send_keys(keys)

    def clink(self, byValue):
            element = self.getElement(byValue)
            element.clink()

    def getTitle(self):
        return self.driver.title

    def quit(self):
        self.driver.quit()
