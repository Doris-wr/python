# Generated by Selenium IDE
import unittest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Test05211(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def tearDown(self):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_05211(self):
    self.driver.get("https://www.baidu.com/")
    self.driver.set_window_size(1382, 744)
    self.driver.find_element(By.ID, "kw").click()
    self.driver.find_element(By.ID, "kw").send_keys("qinniuzhengwei ")
    self.driver.find_element(By.CSS_SELECTOR, ".bdsug-s").click()
    element = self.driver.find_element(By.LINK_TEXT, "资讯")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.XPATH, "//div[@id=\'1\']/h3/a/em").click()
    self.vars["win7092"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win7092"])
    self.driver.find_element(By.CSS_SELECTOR, ".para:nth-child(2)").click()
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.LINK_TEXT, "青春有你第二季").click()
    self.vars["win8539"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win8539"])
    element = self.driver.find_element(By.CSS_SELECTOR, ".lemmaWgt-secondsKnow-gallery-li .video-shadow")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = self.driver.find_element(By.LINK_TEXT, "百度首页")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
if __name__=="__main__":
	unittest.main()
