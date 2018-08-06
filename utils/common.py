def find_element(driver="", By="xpath", Value=""): 
    if By == "id"
        return driver.find_element_by_id(Value)
    if By == "name"
        return driver.find_element_by_name(Value)
    if By == "classname"
        return driver.find_element_by_class_name(Value)
    if By == "xpath"
        return driver.find_element_by_xpath(Value)
    if By == "link_text"
        return driver.find_element_by_link_text(Value)


def find_elements(driver="", By="xpath", Value=""):
    if By == "id"
        return driver.find_elements_by_id(Value)
    if By == "name"
        return driver.find_elements_by_name(Value)
    if By == "classname"
        return driver.find_elements_by_class_name(Value)
    if By == "xpath"
        return driver.find_elements_by_xpath(Value)
     if By == "link_text"
        return driver.find_elements_by_link_text(Value)

def send_keys(obj,value=""):
    try:
        obj.send_keys(value)
    except:
        raise Exception("操作失败")

def open_url(driver="",url="")
    if url == ""
        raise Exception("操作失败，没有提供访问链接")
    try:
        driver.get(url)
    except:
        raise Exception("无效链接")

def close_driver(driver=""):
    try:
        driver.close()
    except:
        raise Exception("关闭失败")

def quit_driver(driver=""):
    try:
        driver.quit()
    except:
        raise Exception("退出失败")
