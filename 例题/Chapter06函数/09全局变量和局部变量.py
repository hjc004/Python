# def test_one():
#     number = 100
#     print('test_one中的number值为:%d' % number)
#
#
# def test_two():
#     number = 200
#     print('test_two中的number值为:%d' % number)
#
#
# # 调用函数
# test_one()
# test_two()

result = 100  # 全局变量

def sum(a, b):
    result = a + b  # 局部变量
    print('函数内的result的值为：', result)  # result在这里是局部变量
    return result


# 调用sum函数
sum(100, 200)
print('函数外的变量result是全局变量，等于', result)
