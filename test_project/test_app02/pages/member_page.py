from appium.webdriver.common.appiumby import AppiumBy

from test_project.test_app02.pages.main_page import MainPage


class UnloadmemberPage(MainPage):
    """成员姓名"""
    #get_name = (AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.TextView")
    #get_name = (AppiumBy.ID,"com.tencent.wework:id/cc2")
    #get_name = (AppiumBy.CLASS_NAME,"android.widget.TextView")
    def get_member_name(self):
        """获取成员姓名"""
        name_list = []
        for el in self.driver.find_elements(by=AppiumBy.CLASS_NAME,value="android.widget.TextView"):
            ll = el.text
            name_list.append(ll)
        print(name_list)
        return name_list
