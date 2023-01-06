try:
    print("-" * 20)
    first_number = input("请输入第1个数：")
    second_number = input("请输入第2个数：")
    print(int(first_number) / int(second_number))
    print("-" * 20)
except ZeroDivisionError:
    print("第2个数不能为0")
