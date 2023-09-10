import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Selectpage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def add_poster(self,poster):
        """添加发帖人"""
        self.driver.find_element(By.CSS_SELECTOR,"#search-posted-by-filter > input").send_keys(poster)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#search-posted-by-body > ul > li:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".search-cta > span.d-button-label").click()
        return self

    def add_date(self):
        """添加发帖时间"""
        self.driver.find_element(By.CSS_SELECTOR, ".search-cta > span.d-button-label").click()
        return self

    def search(self):
        """点击【搜索】"""
        self.driver.find_element(By.CSS_SELECTOR, ".search-cta > span.d-button-label").click()
        return self

    def onlytitle(self):
        """点击仅在标题中匹配"""
        self.driver.find_element(By.CSS_SELECTOR, "matching-title-only").click()
        self.driver.find_element(By.CSS_SELECTOR, ".search-cta > span.d-button-label").click()
        return self

    def get_result_list(self,result)  ->list[list]:
        """获取搜索结果"""
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.ID, "search-result-count")))
        result_list = []
        for element in self.driver.find_elements(By.CSS_SELECTOR, result):
            result_list.append(element.text)
        return result_list

    def get_resultdate(self,testdate):
        """获取帖子发布时间"""
        resultdate = self.driver.find_elements(By.CSS_SELECTOR,"data-time")
        for date in resultdate:
            if testdate < int(date.text):
                return False
        return True