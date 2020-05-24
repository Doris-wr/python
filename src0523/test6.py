from selenium import webdriver
import os
import time
driver=webdriver.Firefox()
file_path='file:///'+os.path.abspath("D:\\课件\\测试\\selenium\\yyy.html")
driver.get(file_path)
inputs=driver.find_element_by_tag_name("input")
for input in inputs:
    if input.get_attribute('type')=='checkbox':
        input.click()
time.sleep(6)
driver.quit()