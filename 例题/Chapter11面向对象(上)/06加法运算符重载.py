# 定义类
class Demo:
    # 定义构造方法
    def __init__(self, obj):
        self.data = obj[:]

    # 实现加法运算方法的重载，将两个列表对应元素相加
    def __add__(self, obj):
        x = len(self.data)
        y = len(obj.data)
        max = x if x > y else y
        number_list = []
        for n in range(max):
            number_list.append(self.data[n] + obj.data[n])
        # 返回包含新列表的实例对象
        return Demo(number_list[:])


# 创建实例对象并初始化
demo_one = Demo([1, 2, 3])
demo_two = Demo([10, 20, 30])
# 执行加法运算，实质是调用__add__方法
demo_sum = demo_one + demo_two
# 显示加法运算后新实例对象的data属性值
print(demo_sum.data)
