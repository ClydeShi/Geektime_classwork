import allure
#有效等价类-P0
#无效等价类-P1
import pytest


from test_project.test_pytest02.test_file import HeroManagement
from test_project.test_pytest02.read_yaml import Runyaml
import conftest

hero_demo = HeroManagement()



@pytest.mark.parametrize("name",Runyaml.run_yaml("yaml_demo.yaml")["name_success"])
@allure.title("姓名的有效等价类")
@pytest.mark.P0
def test_name_success(name):
    hero = hero_demo.create_hero(name, 10, 100)
    assert hero

@pytest.mark.parametrize("name",Runyaml.run_yaml("yaml_demo.yaml")["name_false"])
@allure.title("姓名的无效等价类")
@pytest.mark.P1
def test_name_false(name):
    hero = hero_demo.create_hero(name, 10, 100)
    assert hero == False

@pytest.mark.parametrize("volume",Runyaml.run_yaml("yaml_demo.yaml")["volume_success"])
@allure.title("血量的有效等价类")
@pytest.mark.P0
def test_volume_success(volume):
    hero = hero_demo.create_hero("Testname", volume, 100)
    assert hero

@pytest.mark.parametrize("volume",Runyaml.run_yaml("yaml_demo.yaml")["volume_false"])
@allure.title("血量的无效等价类")
@pytest.mark.P1
def test_volume_false(volume):
    hero = hero_demo.create_hero("Testname", volume, 100)
    assert hero == False

@allure.title("血量的正确边界值")
def test_volume_value_success(new_data_success):
    hero = hero_demo.create_hero("Testname", conftest.new_data_success, 100)
    assert hero

@allure.title("血量的失败边界值")
def test_volume_value_false(new_data_false):
    hero = hero_demo.create_hero("Testname", conftest.new_data_false, 100)
    assert hero == False

@pytest.mark.parametrize("power",Runyaml.run_yaml("yaml_demo.yaml")["power_success"])
@allure.title("攻击力的有效等价类")
@pytest.mark.P0
def test_power_success(power):
    hero = hero_demo.create_hero("Testname", 66, power)
    assert hero

@pytest.mark.parametrize("power",Runyaml.run_yaml("yaml_demo.yaml")["power_false"])
@allure.title("攻击力的无效等价类")
@pytest.mark.P1
def test_power_false(power):
    hero = hero_demo.create_hero("Testname", 66, power)
    assert hero == False