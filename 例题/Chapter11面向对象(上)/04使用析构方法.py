# 定义类
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("--------del--------")


person = Person("老王", 30)
del person
print("---------1---------")
