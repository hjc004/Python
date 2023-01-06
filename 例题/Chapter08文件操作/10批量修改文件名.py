# 批量在文件名前加前缀
import os

flag = 1  # 1表示添加标志  2表示删除标志
folder_name = './'

# 获取指定路径的所有文件名字
dir_list = os.listdir(folder_name)

# 遍历输出所有文件名字
for name in dir_list:
    print(name)
    if flag == 1:
        new_name = '[黑马程序员]-' + name
    elif flag == 2:
        number = len('[黑马程序员]-')
        new_name = name[number:]
    print(new_name)
    os.rename(folder_name + name, folder_name + new_name)
