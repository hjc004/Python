# 定义变量names_list，默认有3个元素
names_list = ['xiaoWang', 'xiaoZhang', 'xiaoHua']
print("-----添加之前，列表names_list的数据-----")
for temp in names_list:
    print(temp)

# 提示并添加元素
temp_name = input('请输入要添加的学生姓名:')
names_list.append(temp_name)
print("-----添加之后，列表names_list的数据-----")
for temp in names_list:
    print(temp)