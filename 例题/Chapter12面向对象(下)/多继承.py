# 定义表示鸟的类
class Bird(object):
    # 飞
    def fly(self):
        print("--鸟儿在天空飞翔--")

    # 呼吸
    # def breathe(self):
    #     print("鸟儿呼吸")


# 定义表示鱼的类
class Fish(object):
    # 游
    def swim(self):
        print("--鱼儿在水中遨游--")

    # 呼吸
    # def breathe(self):
    #     print("鱼儿呼吸")


# 定义表示飞鱼的类
class Volador(Bird, Fish):
    pass


volador = Volador()
volador.fly()
volador.swim()
# volador.breathe()
