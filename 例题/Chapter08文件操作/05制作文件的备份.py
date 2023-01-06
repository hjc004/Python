old_file_name = input("请输入要拷贝的文件名字:")
old_file = open(old_file_name,'r')

# 如果打开文件
if old_file:
    # 提取文件的后缀
    location_flag = old_file_name.rfind('.')
    if location_flag > 0:
        file_flag = old_file_name[location_flag:]
        # 组织新的文件名字
        new_file_name = old_file_name[:location_flag] + '[复件]' + file_flag
        # 创建新文件
        new_file = open(new_file_name, 'w')
        # 把旧文件中的数据，一行一行的进行复制到新文件中
        for line_content in old_file.readlines():
            new_file.write(line_content)

# 关闭文件
old_file.close()
new_file.close()