from selenium import webdriver
import os
import time
driver=webdriver.Firefox()
file_path='file:///'+os.path.abspath("D:\\课件\\测试\\selenium\\frame.html")
driver.get(file_path)
driver.switch_to.frame("f1")
driver.switch_to.frame("f2")
driver.find_element_by_id("kw").send_keys("布拉格")
driver.find_element_by_id("su").click()
time.sleep(8)
driver.quit()