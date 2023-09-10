import pytest

from test_project.test_pytest02.read_yaml import Runyaml

def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的用例名name和用例标识nodeid的中文信息显示在控制台上
    """
    for i in items:
        i.name=i.name.encode("utf-8").decode("unicode_escape")
        i._nodeid=i.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.fixture(params=Runyaml.run_yaml("yaml_demo.yaml")["volume_value_success"])
def new_data_success(request):
    request.param += 1
    return request.param

@pytest.fixture(params=Runyaml.run_yaml("yaml_demo.yaml")["volume_value_false"])
def new_data_false(request):
    request.param += 1
    return request.param
