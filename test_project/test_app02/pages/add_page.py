from appium.webdriver.common.appiumby import AppiumBy
from test_project.test_app02.pages.main_page import MainPage


class AddPage(MainPage):
    """手动输入添加"""
    to_addinfopage = (AppiumBy.XPATH, "//*[@text='手动输入添加']")

    def to_addinfo_page(self):
        """点击手动输入添加"""
        self.click(self.to_addinfopage)