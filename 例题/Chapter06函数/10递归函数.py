def func(count):
    if count == 1:
        result = 1
    else:
        result = func(count - 1) * count
    return result


number = int(input("请输入一个正整数:"))
print("%d！=" % number, func(number))
