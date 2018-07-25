from selenium import webdriver
import time

# 实例化驱动
driver = webdriver.Chrome(executable_path='./Drivers/chromedriver')

# driver.get("183.239.209.132:8081")
# driver.find_element_by_name('UserName').send_keys("admin")
# driver.find_element_by_name('Password').send_keys("admin8118")
# driver.find_element_by_id('btnLogin').click()
# time.sleep(10)

driver.get("httt://www.baidu.com")
driver.find_element_by_name('wd').send_keys("浪晋")
driver.find_element_by_id('su').click()
time.sleep(2)
driver.quit()
