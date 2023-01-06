# 定义类
class Demo:
    # 定义构造方法
    def __init__(self, obj):
        self.data = obj[:]

    # 定义索引、分片运算符重载方法
    def __getitem__(self, index):
        return self.data[index]


# 创建实例对象，用列表初始化
demo = Demo([1, 2, 3, 4])
print(demo[1])  # 索引返回单个值
print(demo[:])  # 分片返回全部的值
print(demo[:2])  # 分片返回部分值
for number in demo:  # for循环迭代
    print(number)
