import time

import pytest
from appium import webdriver
from test_project.test_app02.pages.add_page import AddPage
from test_project.test_app02.pages.addinfo_page import AddinfoPage
from test_project.test_app02.pages.address_page import AddressPage
from test_project.test_app02.pages.main_page import MainPage
from test_project.test_app02.pages.member_page import UnloadmemberPage


def get_wecomdriver():
    """启动企业微信"""
    caps = {}
    caps["appPackage"] = "com.tencent.wework"
    caps["appActivity"] = "com.tencent.wework.launch.LaunchSplashActivity"
    #caps["appActivity"] = "com.tencent.wework.friends.controller.MemberInviteMenuActivity"
    caps["platformName"] = "android"
    caps['settings[waitForIdleTimeout]'] = 0
    caps['noReset'] = True
    #不清除缓存
    caps["appium:ensureWebviewsHavePages"] = True
    caps["appium:nativeWebScreenshot"] = True
    caps["appium:newCommandTimeout"] = 3600
    caps["appium:connectHardwareKeyboard"] = True
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
    driver.implicitly_wait(10)
    return driver

@pytest.fixture(name="wecom")
def init_wecom():
    b = get_wecomdriver()
    yield b
    b.quit()

@pytest.fixture()
def mainpage(wecom):
    return MainPage(wecom)

@pytest.fixture()
def addpage(wecom):
    return AddPage(wecom)

@pytest.fixture()
def addinfopage(wecom):
    return AddinfoPage(wecom)

@pytest.fixture()
def memberpage(wecom):
    return UnloadmemberPage(wecom)

@pytest.fixture()
def addresspage(wecom):
    return AddressPage(wecom)