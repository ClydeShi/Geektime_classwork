import time

from test_project.test_web01.base.base_page import Searchpage


class Test_search:
    def setup_class(self):
        self.search_page = Searchpage()

    def teardown_class(self):
        self.search_page.close()

    def test_search_topic(self):
        """在标题/帖子中搜索"""
        assert "开发" in str(self.search_page.to_search_topic().search("开发").get_searchtopic_result(".fps-result .fps-topic"))

    def test_search_tag(self):
        """在类别/标签中搜索"""
        assert "文章" in str(self.search_page.to_search_tag().search("文章").get_searchtopic_result(".category-name"))

    def test_search_username(self):
        """在用户中搜索"""
        assert "测试" in str(self.search_page.to_search_username().search("测试").get_searchtopic_result(".name"))

    def test_poster(self):
        """搜索作者"""
        poster = "hogwarts"
        list_poster = self.search_page.to_poster("测试").add_poster("hogwarts").get_result_list(".author")
        for i in list_poster:
            if poster not in i:
                return False
            else:
                return True
        assert self.test_poster()

    def test_date(self):
        """搜索发帖时间"""
        testdate = "2023-06-23"
        dt = testdate + " 00:00:00"
        timeim = time.strptime(dt,"%Y-%m-%d %H:%M:%S")
        secs = time.mktime(timeim)
        pa_time = int(secs)*1000
        assert self.search_page.to_add_time(testdate,"测试").search().get_resultdate(pa_time)

    def test_titleonly(self):
        """搜索仅在标题中匹配"""
        search_for = "python"
        list_titles = self.search_page.to_onlytitle_page("python").onlytitle().get_result_list(".topic-title")
        for i in list_titles:
            if search_for not in i:
                return False
            else:
                return True
        assert self.test_titleonly()