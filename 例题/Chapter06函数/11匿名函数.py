# add = lambda a, b: a + b
# # 调用add函数
# print("运行结果：", add(10, 20))
# print("运行结果：", add(20, 20))


# def func(a, b, operation):
#     print("a=%d" % a)
#     print("b=%d" % b)
#     print("result=", operation(a, b))
#
#
# func(11, 22, lambda x, y: x + y)
# print("-------------------")
# func(11, 22, lambda x, y: x - y)


students = [
    {"name": "zhangsan", "age": 18},
    {"name": "lisi", "age": 19},
    {"name": "wangwu", "age": 17}
]
# 按name排序：
students.sort(key=lambda x: x['name'])
print("按name排序后的结果为：", students)
# 按age排序
students.sort(key=lambda x: x['age'])
print("按age排序后的结果为：", students)
