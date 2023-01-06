# 捕获所有的异常
try:
    first_number = input("请输入第1个数：")
    second_number = input("请输入第2个数：")
    print(int(first_number) / int(second_number))
except:
    print("出现错误了")
