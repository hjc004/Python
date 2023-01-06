# 定义变量list_demo，默认有3个元素
list_demo = ['xiaoWang', 'xiaoZhang', 'xiaoHua']
print("-----修改之前，列表list_demo的数据-----")
for temp in list_demo:
    print(temp)

# 修改元素
list_demo[1] = 'xiaoLu'
print("-----修改之后，列表list_demo的数据-----")
for temp in list_demo:
    print(temp)
