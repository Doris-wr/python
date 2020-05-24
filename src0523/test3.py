from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Firefox()
driver.get("https://1270.0.1/biz/user-login-LZJpei8=.html")
driver.implicitly_wait(10)
driver.find_element_by_id("account").send_keys("admin")
driver.find_element_by_id("account").send_keys(Keys.TAB)
time.sleep(3)
driver.find_element_by_name("password").send_keys("h0")
time.sleep(6)
driver.find_element_by_name("password").send_keys(Keys.ENTER)
time.sleep(6)
driver.quit()

