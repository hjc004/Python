# 定义一个动物类
class Animal(object):
    def __init__(self, color="白色"):
        self.__color = color  # 颜色

    def __test(self):  # 私有方法
        print(self.__color)

    def test(self):  # 测试方法
        print(self.__color)


# 定义一个动物的子类狗
class Dog(Animal):
    def dog_test_one(self):
        print(self.__color)  # 访问父类的私有属性

    def dog_test_two(self):
        self.__test()  # 访问父类的私有方法
        self.test()  # 访问父类的公有方法


dog = Dog("深棕色")
# dog.dog_test_one()
dog.dog_test_two()
