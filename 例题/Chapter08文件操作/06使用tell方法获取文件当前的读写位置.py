# 打开一个已经存在的文件
file = open("itheima.txt", "r")
words = file.read(4)
print("读取的数据是 : ", words)

# 查找当前位置
position = file.tell()
print("当前文件位置 : ", position)
words = file.read(8)
print("读取的数据是 : ", words)

# 查找当前位置
position = file.tell()
print("当前文件位置 : ", position)
words = file.read(3)
print("读取的数据是 : ", words)

# 查找当前位置
position = file.tell()
print("当前文件位置 : ", position)
file.close()