import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestPRUEBAS():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_pRUEBAS(self):
    self.driver.get("https://9cbe8f83-6690-4868-8e78-331b3c9351c7.serverhub.tripleten-services.com/")
    self.driver.set_window_size(1920, 1057)
    self.driver.find_element(By.CSS_SELECTOR, ".dst-picker-row:nth-child(1) .label").click()
    self.driver.find_element(By.ID, "from").send_keys("east 2nd street 601")
    self.driver.find_element(By.ID, "to").click()
    self.driver.find_element(By.ID, "to").send_keys("1300 1st st")
    self.driver.find_element(By.CSS_SELECTOR, ".button:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".tcard:nth-child(5) > .tcard-icon > img").click()
    self.driver.find_element(By.CSS_SELECTOR, ".np-text").click()
    self.driver.find_element(By.CSS_SELECTOR, ".active .label").click()
    self.driver.find_element(By.ID, "phone").send_keys("+1 123 123 12 12")
    self.driver.find_element(By.CSS_SELECTOR, ".active .button").click()
    self.driver.find_element(By.CSS_SELECTOR, ".active:nth-child(2) > .close-button").click()
    self.driver.find_element(By.CSS_SELECTOR, ".pp-text").click()
    self.driver.find_element(By.CSS_SELECTOR, ".disabled > .pp-title").click()
    self.driver.find_element(By.ID, "number").click()
    self.driver.find_element(By.ID, "number").send_keys("1234 5678 9011")
    self.driver.find_element(By.NAME, "code").click()
    self.driver.find_element(By.NAME, "code").send_keys("111")
    self.driver.find_element(By.CSS_SELECTOR, ".unusual > form").click()
    self.driver.find_element(By.CSS_SELECTOR, ".pp-buttons > .button:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".payment-picker .active > .close-button").click()
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) > .input-container").click()
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) > .input-container > .label").click()
    self.driver.find_element(By.ID, "comment").send_keys("muestrAME EL CAMINO")
    self.driver.find_element(By.CSS_SELECTOR, ".r:nth-child(1) .slider").click()
    self.driver.find_element(By.CSS_SELECTOR, ".r:nth-child(1) .counter-plus").click()
    self.driver.find_element(By.CSS_SELECTOR, ".r:nth-child(1) .counter-plus").click()
    self.driver.find_element(By.CSS_SELECTOR, ".smart-button-main").click()
    self.driver.close()
  

  



