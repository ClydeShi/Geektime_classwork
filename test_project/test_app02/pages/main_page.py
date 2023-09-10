from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class MainPage:

    def __init__(self,driver):
        self.driver = driver

    def click(self,ele):
        """点击"""
        wait = WebDriverWait(self.driver, 15, 0.5)
        element = wait.until(ec.presence_of_element_located(ele))
        ActionChains(self.driver).click(element).perform()
        # el = self.driver.find_element(*ele)
        # el.click()

    def send_keys(self,ele,keyword):
        """输入"""
        el = self.driver.find_element(*ele)
        el.send_keys(keyword)

    def back(self):
        """返回"""
        #self.click(self.to_back)
        self.driver.back()


