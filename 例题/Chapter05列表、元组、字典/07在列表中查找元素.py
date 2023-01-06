# 待查找的列表
name_list = ['xiaoWang', 'xiaoZhang', 'xiaoHua']

# 获取用户要查找的名字
find_name = input('请输入要查找的姓名:')

# 查找是否存在
if find_name in name_list:
    print('在列表中找到了相同的名字')
else:
    print('没有找到')
