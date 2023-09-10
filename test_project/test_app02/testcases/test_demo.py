import time

from test_project.test_app02.pages.add_page import AddPage
from test_project.test_app02.pages.addinfo_page import AddinfoPage
from test_project.test_app02.pages.address_page import AddressPage
from test_project.test_app02.pages.main_page import MainPage
from test_project.test_app02.pages.member_page import UnloadmemberPage


class Test_demo:

    def test_add_success(self,mainpage:MainPage,addresspage:AddressPage,addpage:AddPage, addinfopage:AddinfoPage, memberpage:UnloadmemberPage):
        """添加成员成功"""
        addresspage.to_address_page()
        addresspage.to_add_page()
        addpage.to_addinfo_page()
        addinfopage.input_name("张三")
        addinfopage.input_tel("12345678998")
        addinfopage.save_new()
        time.sleep(2)
        mainpage.back()
        addresspage.to_unloadmember_page()
        time.sleep(1)
        assert "张三" in memberpage.get_member_name()

    def test_add_name_none(self,mainpage:MainPage,addresspage:AddressPage,addpage:AddPage,addinfopage:AddinfoPage):
        """添加成员姓名为空"""
        addresspage.to_address_page()
        addresspage.to_add_page()
        addpage.to_addinfo_page()
        addinfopage.input_tel("12345678998")
        addinfopage.save_new()
        time.sleep(1)
        assert addinfopage.get_errorinfo() == "姓名不能为空"

    def add_tel_none(self,mainpage:MainPage,addresspage:AddressPage,addpage:AddPage,addinfopage:AddinfoPage):
        """添加成员手机为空"""
        addresspage.to_address_page()
        addresspage.to_add_page()
        addpage.to_addinfo_page()
        addinfopage.input_name("张三")
        addinfopage.save_new()
        time.sleep(1)
        assert addinfopage.get_errorinfo() == "手机号不能为空"

    def test_wrongtel(self,mainpage:MainPage,addresspage:AddressPage,addpage:AddPage,addinfopage:AddinfoPage):
        """错误成员手机"""
        addresspage.to_address_page()
        addresspage.to_add_page()
        addpage.to_addinfo_page()
        addinfopage.input_name("张三")
        addinfopage.input_tel("123")
        addinfopage.save_new()
        time.sleep(1)
        assert addinfopage.get_errorinfo() == "请填写合法的手机号"

    def test_addmore(self,mainpage:MainPage,addresspage:AddressPage,addpage:AddPage,addinfopage:AddinfoPage,memberpage:UnloadmemberPage):
        """继续添加多个"""
        addresspage.to_address_page()
        addresspage.to_add_page()
        addpage.to_addinfo_page()
        addinfopage.input_name("张2三")
        addinfopage.input_tel("12345678998")
        addinfopage.save_more()
        time.sleep(1)
        addinfopage.input_name("张3三")
        addinfopage.input_tel("12345678999")
        addinfopage.save_new()
        time.sleep(2)
        mainpage.back()
        mainpage.back()
        addresspage.to_unloadmember_page()
        time.sleep(1)
        assert "张2三" in memberpage.get_member_name()
        assert "张3三" in memberpage.get_member_name()

    def test_delmember(self,addresspage:AddressPage,addinfopage:AddinfoPage):
        addresspage.to_address_page()
        addinfopage.del_member("张三")
        assert True