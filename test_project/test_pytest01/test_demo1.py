import pytest

from test_project.test_pytest01.test_file import HeroManagement

hero_demo = HeroManagement()

#姓名的有效等价类
@pytest.mark.parametrize("name",["1","TTT","%^&*"])
def test_name_success(name):
    hero = hero_demo.create_hero(name, 55, 100)
    assert hero

#姓名的无效等价类
@pytest.mark.parametrize("name",[1, False ,55.55])
def test_name_false(name):
    hero = hero_demo.create_hero(name, 55, 100)
    assert hero == False

#血量的有效等价类
@pytest.mark.parametrize("volume",[1,99])
def test_volume_success(volume):
    hero = hero_demo.create_hero("Testname", volume, 100)
    assert hero

#血量的无效等价类
@pytest.mark.parametrize("volume",["aa",False])
def test_volume_false(volume):
    hero = hero_demo.create_hero("Testname", volume, 100)
    assert hero == False

#血量的正确边界值
@pytest.mark.parametrize("volume",[1,2,98,99])
def test_volume_value_success(volume):
    hero = hero_demo.create_hero("Testname", volume, 100)
    assert hero

#血量的失败边界值
@pytest.mark.parametrize("volume",[-3,0,100])
def test_volume_value_false(volume):
    hero = hero_demo.create_hero("Testname", volume, 100)
    assert hero == False

#攻击力的有效等价类
@pytest.mark.parametrize("power",[1,99])
def test_power_success(power):
    hero = hero_demo.create_hero("Testname", 66, power)
    assert hero

#攻击力的无效等价类
@pytest.mark.parametrize("power",["aa",False,55.55,0,-1])
def test_power_false(power):
    hero = hero_demo.create_hero("Testname", 66, power)
    assert hero == False