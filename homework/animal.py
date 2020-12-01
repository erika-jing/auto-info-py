'''课后作业
1、自己写一个面向对象的例子：
比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
复写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发=短毛，
添加一个新的方法， 会捉老鼠，
复写父类的‘【会叫】的方法，改成【喵喵叫】
创建子类【狗】，继承【动物类】，
复写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发=长毛，
添加一个新的方法， 会看家，
复写父类的【会叫】的方法，改成【汪汪叫】
调用 name== ‘main’：
创建一个猫猫实例
调用捉老鼠的方法
打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。
创建一个狗狗实例
调用【会看家】的方法
打印【狗狗的姓名，颜色，年龄，性别，毛发】。
2、将数据配置到yaml文件里
'''

import yaml

# 定义一个animal类
class Animal():

    # 初始化四个属性
    def __init__(self,name,color,age,gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    #添加动物run方法
    def run(self):
        print("动物会跑")

    # 添加动物scream方法
    def scream(self):
        print("动物会叫")

# 定义一个cat类，继承animal父类及其属性
class Cat(Animal):

    # 多添加一个短毛属性
    def __init__(self,name,color,age,gender,shorthair):
        self.shorthair = shorthair
        super().__init__(name,color,age,gender)

     # 改成喵喵叫
    def scream(self):
            print("小猫喜欢喵喵叫")

    # 添加cat捉老鼠方法
    def catch(self):
        print("小猫的技能是捉老鼠")
        print(f"{c_name}捉到了老鼠,她是一只年龄{c_age}岁，{c_shothair}{c_color}的小猫咪，性别是{c_gender}")
        print("\n")



# 定义一个dog类，继承animal父类及其属性
class Dog(Animal):

#继承父类，并添加长毛新属性
    def __init__(self,name,color,age,gender,longhair):
        self.longhair = longhair
        super().__init__(name, color, age, gender)

#改成汪汪叫
    def scream(self):
        print(("小狗会汪汪叫"))

#添加dog看家方法
    def Look(self):
        print("小狗的技能是看家")
        print(f"{d_name}会看家,他是一只年龄{d_age}岁，{d_longhair}{d_color}的小狗，性别是{d_gender}")
        print("\n")

if __name__ == '__main__':
     A = Animal("", "", "", "")
     A.run()
     A.scream()
     print("\n")
     with open("animal_data.yml",encoding="UTF-8") as f:
         datas = yaml.safe_load(f)

    # 小猫的数据
     c_name = datas['cat_datas']['name']
     c_color = datas['cat_datas']['color']
     c_age = datas['cat_datas']['age']
     c_gender = datas['cat_datas']['gender']
     c_shothair = datas['cat_datas']['shorthair']

     c = Cat(c_name,c_color,c_age,c_gender,c_shothair)
     c.scream()
     c.catch()


     # 小狗的数据
     d_name = datas['dog_datas']['name']
     d_color = datas['dog_datas']['color']
     d_age = datas['dog_datas']['age']
     d_gender = datas['dog_datas']['gender']
     d_longhair = datas['dog_datas']['longhair']

     d = Dog(d_name,d_color,d_age,d_gender,d_longhair)
     d.scream()
     d.Look()

