from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get("https://www.baidu.com") 

driver.find_element_by_id("kw").send_keys("清明节")
driver.find_element_by_id("su").click()
time.sleep(8)
js="var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(6)
js="var q=document.documentElement.scrollTop=0"
driver.execute_script(js)
time.sleep(6)
driver.quit()
