from appium.webdriver.common.appiumby import AppiumBy

from test_project.test_app02.pages.main_page import MainPage


class AddressPage(MainPage):
    """添加成员按钮"""
    to_addpage = (AppiumBy.XPATH, '//*[@text= "添加成员"]')

    """未加入的成员"""
    to_unloadmember = (AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[3]")

    """通讯录按钮"""
    to_address = (AppiumBy.XPATH, "//*[@text= '通讯录']")
    #to_address = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[5]/android.widget.RelativeLayout/android.widget.TextView")

    def to_address_page(self):
        """通讯录页面"""
        self.click(self.to_address)

    def to_add_page(self):
        """点击添加成员"""
        self.click(self.to_addpage)

    def to_unloadmember_page(self):
        """查看未加入成员"""
        self.click(self.to_unloadmember)