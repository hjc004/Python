try:
    first_number = input("请输入第1个数：")
    second_number = input("请输入第2个数：")
    print(int(first_number) / int(second_number))
except ZeroDivisionError:
    print("第2个数不能为0")
except ValueError:
    print("只能输入数字")
