# 定义Cat类
class Cat(object):
    # 类属性
    number = 0

    def __init__(self):
        # 实例属性
        self.age = 1
        # self.number = 100


cat = Cat()
# 用对象去访问类属性是可以的
print(cat.number)
# 常用的方式是，使用类去访问类属性
print(Cat.number)
