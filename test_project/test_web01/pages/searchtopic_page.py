import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Searchtopicpage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def search(self,keyword)  ->'Searchtopicpage':
        """输入搜索内容点击搜索"""
        self.driver.find_element(By.CSS_SELECTOR, "input.full-page-search").send_keys(keyword)
        self.driver.find_element(By.CSS_SELECTOR, ".search-cta > span.d-button-label").click()
        return self

    def get_searchtopic_result(self,result)  ->list[list]:
        """获取帖子搜索结果"""
        time.sleep(3)
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "search-result-count")))
        title_list = []
        for element in self.driver.find_elements(By.CSS_SELECTOR, result):
            title_list.append(element.text)
        return title_list