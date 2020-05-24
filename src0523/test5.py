# 鼠标事件
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
driver=webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.find_element_by_id("kw").send_keys("清明节")
su=driver.find_element_by_id("su")
# 右击
ActionChains(driver).context_click(su).perform()
time.sleep(6)
# 双击
ActionChains(driver).double_click(su).perform()
time.sleep(6)
driver.quit()
