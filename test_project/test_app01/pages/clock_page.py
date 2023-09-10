import time

from appium.webdriver.common.appiumby import AppiumBy
from test_project.test_app01.pages.main_page import MainPage

class ClockPage(MainPage):
    """添加按钮"""
    add_stn = (AppiumBy.ACCESSIBILITY_ID,"Cities")

    """城市输入框"""
    send_city= (AppiumBy.ID, "com.google.android.deskclock:id/search_src_text")

    """选择选项"""
    add_citys = (AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.TextView[1]")

    def search_city(self, keyword):
        """添加城市时间"""
        #self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Cities").click()
        #self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Cities").click()
        self.click(self.add_stn)
        #self.driver.find_element(by=AppiumBy.ID, value="com.google.android.deskclock:id/search_src_text").send_keys(keyword)
        self.send_keys(self.send_city,keyword)

    def add_city(self):
        """点击添加城市选项"""
        self.click(self.add_citys)
        time.sleep(1)

    def get_cityname(self):
        """获取已添加的city name"""
        city_list = []
        for eles in self.driver.find_elements(by=AppiumBy.ID,value="com.google.android.deskclock:id/city_name"):
            l = eles.text
            city_list.append(l)
        print(f"已添加的城市有：{city_list}")
        return city_list

    def get_fail(self):
        """获取无数据文案"""
        fail_test = self.driver.find_element(AppiumBy.ID,"com.google.android.deskclock:id/search_empty_view")
        return fail_test.text