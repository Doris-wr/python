from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.find_element_by_name("tj")
# driver.find_element_by_id("kw").send_keys("金士杰")
# time.sleep(6)
# driver.find_element_by_id("kw").clear()
# driver.find_element_by_id("kw").send_keys("刘亦菲")
# driver.find_element_by_id("su").submit()
time.sleep(8)
driver.quit()
