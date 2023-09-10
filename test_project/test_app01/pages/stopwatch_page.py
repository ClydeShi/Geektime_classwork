import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from test_project.test_app01.pages.main_page import MainPage


class StopWatchPage(MainPage):
    """watch入口按钮"""
    watch = (AppiumBy.ACCESSIBILITY_ID,'Stopwatch')

    """启动按钮"""
    start = (AppiumBy.ACCESSIBILITY_ID,'Start')

    """结束按钮"""
    pause = (AppiumBy.ACCESSIBILITY_ID,'Pause')

    """增加计时按钮"""
    lap = (AppiumBy.ACCESSIBILITY_ID,'Lap')

    """归零按钮"""
    reset = (AppiumBy.ACCESSIBILITY_ID,'Reset')

    def to_watch(self):
        self.click(self.watch)
        return self


    def run_stopwatch(self):
        """单次启动和结束"""
        #driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Start")
        self.click(self.start)
        time.sleep(1)
        #driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Pause")
        self.click(self.pause)
        time.sleep(1)

    def run_lap(self):
        """多次增加中间时间"""
        #driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Start")
        self.click(self.start)
        time.sleep(1)
        #driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Lap").click()
        self.click(self.lap)
        time.sleep(1)
        #driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Lap").click()
        self.click(self.lap)
        time.sleep(1)
        #driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Pause")
        self.click(self.pause)
        time.sleep(1)

    def run_reset(self):
        """归零"""
        #driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Start")
        self.click(self.start)
        time.sleep(1)
        #driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Pause")
        self.click(self.pause)
        time.sleep(1)
        #driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Reset")
        self.click(self.reset)
        time.sleep(1)

    def get_pasue_time(self):
        """获取结束时间"""
        pasuetime = self.driver.find_element(AppiumBy.ID, "com.google.android.deskclock:id/stopwatch_time_text").text
        hundredths = self.driver.find_element(AppiumBy.ID, "com.google.android.deskclock:id/stopwatch_hundredths_text").text
        time_text = pasuetime + ':' + hundredths
        return time_text

    def get_lap_time(self):
        """获取中间时间"""
        laptime = self.driver.find_element(AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.TextView[3]")
        return laptime.text

