# 定义类
class Demo:
    data_one = 100

    # 定义为属性data_two赋值的方法
    def set(self, number):
        self.data_two = number

    # 重载方法
    def __str__(self):
        # 返回自定义的字符串
        return 'data_one=%s; data_two=%s' % (self.data_one, self.data_two)


# 创建实例对象
demo = Demo()
# 调用方法给属性赋值，并创建属性
demo.set(200)
print(demo)  # 调用__str__方法进行转换
print(str(demo))  # 调用repr函数，结果显示没有进行转换
print(repr(demo))  # 调用__str__方法进行转换
