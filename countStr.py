# File:countStr.py
# 统计字符串中数字，大小写字母个数

a = input("Please input string:")
intCount = 0
big_letterCount = 0
small_letterCount = 0

for i in a:
    if i.isdigit():
        intCount += 1
    elif i.isupper():
        big_letterCount += 1
    elif i.islower():
        small_letterCount += 1

print("数字%d个，大写字母%d个，小写字母%d个" % (intCount,big_letterCount,small_letterCount))
