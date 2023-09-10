import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from test_project.test_app01.pages.clock_page import ClockPage
from test_project.test_app01.pages.main_page import MainPage
from test_project.test_app01.pages.stopwatch_page import StopWatchPage


def get_driver():
    """启动app"""
    caps = {}
    caps["appPackage"] = "com.google.android.deskclock"
    caps["appActivity"] = "com.android.deskclock.DeskClock"
    caps["platformName"] = "android"
    caps['settings[waitForIdleTimeout]'] = 0
    caps["appium:ensureWebviewsHavePages"] = True
    caps["appium:nativeWebScreenshot"] = True
    caps["appium:newCommandTimeout"] = 3600
    caps["appium:connectHardwareKeyboard"] = True
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
    driver.implicitly_wait(5)
    return driver

@pytest.fixture(name="app")
def init_app():
    a = get_driver()
    yield a
    a.quit()

@pytest.fixture()
def mainpage(app):
    return MainPage(app)

@pytest.fixture()
def clockpage(app):
    return ClockPage(app)

@pytest.fixture()
def stopwatchpage(app):
    return StopWatchPage(app)