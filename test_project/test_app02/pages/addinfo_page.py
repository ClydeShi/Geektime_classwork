from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from test_project.test_app02.pages.main_page import MainPage


class AddinfoPage(MainPage):
    """姓名输入框"""
    name = (AppiumBy.ID,"com.tencent.wework:id/c4i")

    """手机号输入框"""
    tel = (AppiumBy.ID, "com.tencent.wework:id/ig9")

    """保存按钮"""
    save = (AppiumBy.ID,"com.tencent.wework:id/b2r")

    """保存并继续添加按钮"""
    savemore = (AppiumBy.ID,"com.tencent.wework:id/b2s")

    def input_name(self,name_key):
        """输入名字"""
        self.send_keys(self.name,name_key)

    def input_tel(self,tel_key):
        """输入手机"""
        self.send_keys(self.tel,tel_key)

    def save_new(self):
        """点击保存"""
        self.click(self.save)

    def save_more(self):
        """点击保存并继续添加"""
        self.click(self.savemore)

    def get_errorinfo(self):
        """获取错误提示"""
        el = self.driver.find_element(AppiumBy.ID,"com.tencent.wework:id/cqh").text
        return el

    def del_member(self,delname):
        """删除通讯录"""

        """待删除用户"""
        deltext = "//*[@text='" + delname + "']"
        delmember = (AppiumBy.XPATH,deltext)
        self.driver.find_element(by=AppiumBy.XPATH,value=deltext).click()
        self.click(delmember)
        #self.click(delmember)
        self.driver.find_element(by=AppiumBy.ID, value="com.tencent.wework:id/ll9").click()
        self.driver.find_element(by=AppiumBy.ID, value="com.tencent.wework:id/cb9").click()

        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(924, 1722)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(955, 722)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

        self.driver.find_element(by=AppiumBy.ID, value="com.tencent.wework:id/h0w").click()
        self.driver.find_element(by=AppiumBy.ID, value="com.tencent.wework:id/czz").click()