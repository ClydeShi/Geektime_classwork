from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class MainPage:
    def __init__(self,driver):
        self.driver = driver

    def click(self,ele):
        """点击"""
        #self.driver.find_element(*ele).click()
        wait = WebDriverWait(self.driver,5,0.5)
        element = wait.until(ec.element_to_be_clickable(ele))
        ActionChains(self.driver).click(element).perform()

    def send_keys(self,ele,keyword):
        """输入"""
        el =self.driver.find_element(*ele)
        el.send_keys(keyword)


