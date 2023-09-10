import sys
hero_list = []

class Hero_demo:
    def hero_create(self):
        """创建英雄"""
        hero_name = input("编辑新英雄名称：")
        hero_hp = input("编辑新英雄血量：")
        hero_power = input("编辑新英雄攻击力：")
        hero_new = {"name": hero_name, "hp": hero_hp, "power": hero_power}
        hero_list.append(hero_new)
        print(f"新建英雄成功^_^该英雄数据为：{hero_new}")
        return hero_list

    def hero_search(self):
        """搜索英雄数据"""
        hero_info = input("待查询角色的名称：")
        if hero_info == "q":
            return
        else:
            for h in hero_list:
                if hero_info == h["name"]:
                    print(f"英雄数据为:{h}")
                    return True
            print("查询失败，重新输入\n————输入【q】退出查询")
            return self.hero_search()

    def hero_change(self):
        """修改英雄数据"""
        hero_cha = input("待更新数据英雄的名称：")
        if hero_cha == "q":
            return
        else:
            for h in hero_list:
                    if hero_cha == h["name"]:
                        print(f"英雄数据为:{h}")
                        hero_new_hp = input(("修改后的血量为："))
                        h["hp"] = hero_new_hp
                        print(f"英雄{hero_cha}的血量修改成功^_^最新数据为{h}")
                        return
            print("查询失败,重新输入\n————输入【q】退出修改")
            return self.hero_change()

    def hero_delete(self):
        """删除英雄"""
        hero_del = input("待删除英雄的名称：")
        if hero_del == "q":
            return
        else:
            for h in hero_list:
                if hero_del == h["name"]:
                    hero_list.remove(h)
                    print(f"已成功删除英雄:{hero_del}")
                    return
            print("查询失败,重新输入\n————输入【q】退出修改")
            return self.hero_delete()

    def exit(self):
        print("————< 已退出程序 >————")
        sys.exit(1)

herodemo = Hero_demo()

while True:
    """明确指令"""
    print("+++指令集合：1.新建 _ 2.查询 _ 3.修改 _ 4.删除 _ 5.退出")
    order = input("请输入操作指令：")
    if order == "1":
        herodemo.hero_create()
    elif order == "2":
        herodemo.hero_search()
    elif order == "3":
        herodemo.hero_change()
    elif order == "4":
        herodemo.hero_delete()
    elif order == "5":
        herodemo.exit()
    else:
        print("xxx指令错误，重新输入xxx")