import time
import pytest
from test_project.test_app01.base.read_data import Runyaml
from test_project.test_app01.pages.clock_page import ClockPage
from test_project.test_app01.pages.main_page import MainPage
from test_project.test_app01.pages.stopwatch_page import StopWatchPage


class Test_Po:
    """成功用例"""
    add_city = Runyaml.run_yaml("testdata.yaml")["add_city"]

    """失败用例"""
    city_fail = Runyaml.run_yaml("testdata.yaml")["city_fail"]

    @pytest.mark.parametrize("add_city", add_city)
    def test_clock_addcity(self,add_city, mainpage: MainPage,
                           clockpage: ClockPage, ):
        """添加城市时间成功"""
        clockpage.search_city(add_city)
        clockpage.add_city()
        print(f"添加{add_city}城市时间成功")
        assert add_city in clockpage.get_cityname()

    @pytest.mark.parametrize("cityfail",city_fail)
    def test_clock_addfail(self, cityfail,mainpage: MainPage,
                           clockpage: ClockPage, ):
        """添加城市时间失败"""
        clockpage.search_city(cityfail)
        time.sleep(1)
        print(f"查询{cityfail}城市失败")
        assert clockpage.get_fail() == "Search for a city"

    def test_stopwatch(self,stopwatchpage:StopWatchPage,
                       clockpage:ClockPage):
        """启停秒表"""
        stopwatchpage.to_watch().run_stopwatch()
        timetime = stopwatchpage.get_pasue_time()
        print(f"结束时间为：{timetime}")
        assert timetime

    def test_laptime(self,stopwatchpage:StopWatchPage,
                       clockpage:ClockPage):
        """多次增加中间时间"""
        stopwatchpage.to_watch().run_lap()
        timetime = stopwatchpage.get_lap_time()
        print(f"插入的时间为：{timetime}")
        assert timetime

    def test_reset(self,stopwatchpage:StopWatchPage,
                       clockpage:ClockPage):
        """归零"""
        stopwatchpage.to_watch().run_reset()
        timetime = stopwatchpage.get_pasue_time()
        print(f"清空后的时间为：{timetime}")
        assert timetime == "0:00"
