'''
1､编写一个程序，输入N个学生信息用字典保存，学生信息有：学号、姓名、性别。
根据学号从小到大输出学生全部信息。
'''

dic = {}

i=0

N= input("输入学生数量：")

while i<N:

     number = input("输入学生学号：")

     name = input("输入学生姓名：")

     dic.__setitem__(number,name)

     i+=1

print("排序前：%s"%dic)

def dict2list(dic:dict):

    ''' 将字典转化为列表 '''

    keys = dic.keys()

    vals = dic.values()

    lst = [(key, val) for key, val in zip(keys, vals)]

    return lst

new = sorted(dict2list(dic), key=lambda x:x[0], reverse=False)

print("排序后：%s"%new)

