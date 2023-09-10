import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from test_project.test_web01.pages.searchtopic_page import Searchtopicpage
from test_project.test_web01.pages.select_page import Selectpage


class Searchpage:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://ceshiren.com/search?expanded=true')
        self.driver.set_window_size(1920, 1055)

    def click(self,eiement):
        self.driver.find_element(By.CSS_SELECTOR,eiement).click()

    def teardown_method(self,):
        self.driver.quit()

    def to_search_topic(self)  ->'Searchtopicpagr':
        """点击展开话题/帖子选项"""
        self.click("#search-type-header > .select-kit-header-wrapper")
        self.click(".select-kit-row[title='话题/帖子']")
        time.sleep(1)
        return Searchtopicpage(self.driver)


    def to_search_tag(self)  ->'Searchtagpage':
        """点击选择【类别/标签】"""
        self.click("#search-type-header > .select-kit-header-wrapper")
        time.sleep(1)
        self.click(".select-kit-row[data-index='1']")
        return Searchtopicpage(self.driver)

    def to_search_username(self)  ->'Searchtagpage':
        """点击选择【用户】"""
        self.click("#search-type-header > .select-kit-header-wrapper")
        time.sleep(1)
        self.click(".select-kit-row[data-index='2']")
        return Searchtopicpage(self.driver)

    def to_poster(self,keyword)  ->'Selectserpage':
        """点击选择【发帖人】"""
        self.driver.find_element(By.CSS_SELECTOR, ".full-page-search").send_keys(keyword)
        self.click("#search-posted-by-header > div")
        return Selectpage(self.driver)

    def to_onlytitle_page(self,keyword)  ->'Selectserpage':
        """点击选择【仅在标题中【匹配】"""
        self.driver.find_element(By.CSS_SELECTOR, ".full-page-search").send_keys(keyword)
        return Selectpage(self.driver)

    def to_add_time(self,date,keyword)  ->'Selectserpage':
        """点击选择【发布时间】"""
        self.driver.find_element(By.CSS_SELECTOR, "input.full-page-search").send_keys(keyword)
        self.driver.find_element(By.CSS_SELECTOR,"#search-post-date").send_keys(date)
        return Selectpage(self.driver)

    def close(self):
        time.sleep(10)
        self.driver.quit()


