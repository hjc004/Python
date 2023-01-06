file = open("itheima.txt", "r")
words = file.read(15)
print("读取的数据是:", words)

# 查找当前位置
position = file.tell()
print("当前文件的位置是：", position)

# 重新设置位置
file.seek(4)

# 查找当前位置
position = file.tell()
print("当前文件的位置是：", position)
file.close()
