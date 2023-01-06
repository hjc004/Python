try:
    first_number = input("请输入第1个数：")
    second_number = input("请输入第2个数：")
    print(int(first_number) / int(second_number))
# 获取描述信息
except (ZeroDivisionError, ValueError) as result:
    print("捕捉到异常:%s" % result)
