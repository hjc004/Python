class Person:
    def __init__(self, name, age):
        self.name = name  # 姓名
        self.__age = age  # 年龄

    # 给私有属性赋值
    def set_age(self, new_age):
        # 判断传入的参数是否符合要求
        if new_age > 0 and new_age <= 120:
            self.__age = new_age

    # 获取私有属性的值
    def get_age(self):
        return self.__age


# 创建对象
person = Person("老王", 30)
# print(person.__age)
person.set_age(31)
print(person.get_age())