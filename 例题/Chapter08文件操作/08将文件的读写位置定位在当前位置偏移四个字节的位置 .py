# 打开一个已经存在的文件
file = open("itheima.txt", "rb+")
words = file.read(15)
print("读取的数据是 : ", words)

# 查找当前位置
position = file.tell()
print("当前文件位置 : ", position)

# 重新设置位置
file.seek(5,1)

# 查找当前位置
position = file.tell()
print("当前文件位置 : ", position)
file.close()