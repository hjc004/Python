# 导入库
import numpy as np
import pandas as pd
from _operator import index
import os


# 扫描文件夹目录
def printPath(level, path):
    global allFileNum

    # 所有文件夹，第一个字段是次目录的级别
    dirList = []
    # 所有文件
    fileList = []
    # 返回一个列表，其中包含在目录条目的名称
    files = os.listdir(path)
    # 先添加目录级别
    dirList.append(str(level))
    for f in files:
        if (os.path.isdir(path + '/' + f)):
            # 排除隐藏文件夹。因为隐藏文件夹过多
            if (f[0] == '.'):
                pass
            else:
                # 添加非隐藏文件夹
                dirList.append(f)
        if (os.path.isfile(path + '/' + f)):
            # 添加文件
            fileList.append(f)
            # 当一个标志使用，文件夹列表第一个级别不打印
    i_dl = 0
    for dl in dirList:
        if (i_dl == 0):
            i_dl = i_dl + 1
        else:
            # 打印至控制台，不是第一个的目录
            print
            '-' * (int(dirList[0])), dl
            # 打印目录下的所有文件夹和文件，目录级别+1
            printPath((int(dirList[0]) + 1), path + '/' + dl)
    for fl in fileList:
        # 打印文件
        print
        '-' * (int(dirList[0])), fl


if __name__ == '__main__':
    printPath(1, 'C:/Users/melon/Desktop/15193005zo67/data')  ###把这里地址改成目标文件夹
    print
    '总文件数 =', allFileNum

# read CSV file
data = pd.read_csv('C:/Users/melon/Desktop/15193005zo67/data/AA00001.csv')  # 放文件目录

# 数据去重
result_noDup = data.drop_duplicates()
# 按指定字段去除重复数据
data_drop = data.drop_duplicates(['lng', 'lat'])
print(data_drop)

# 将结果存CSV

file_folder = 'C:\\Users\\Administrator\\Desktop\\File\\Filename'  ##文件夹位置
if os.path.isdir(file_folder):
    for fileName in os.listdir(file_folder):  # print fileName
        info(fileName)  ##读取文件名字

with open("Ex_info.csv", "ab+") as csvfile:
    csvfile.write(codecs.BOM_UTF8)  ##存入表内的文字格式
    writer = csv.writer(csvfile)  # 存入表时所使用的格式
    writer.writerow(['表头', '表头', '表头', '表头'])  # 自己定义
    writer.writerows(info)  # 写入表