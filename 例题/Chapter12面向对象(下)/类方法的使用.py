class Test(object):
    # 类属性
    number = 0

    # 类方法
    @classmethod
    def set_number(cls, new_number):
        cls.number = new_number


Test.set_number(300)
print(Test.number)
