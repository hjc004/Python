'''
1、编写一个函数，输入三边的长度作为参数，计算三角形的面积。
（要求有三边是否为三角形的判断）

2、 已知一个字典包含多个员工的信息（姓名、性别），请编写多个函数：
增加、删除、修改和查询的员工信息。
'''

1.

import math



def main():



    print("用来判断是否为三角形，并求三角形面积")



    a=int(input("三角形a边长度为："))

    b=int(input("三角形b边长度为："))

    c=int(input("三角形c边长度为："))

    

    if area(a,b,c) :

        print("这是一个三角形面积是：",area(a,b,c))

    else:

        print("这不是一个三角形")  



    



def area(a,b,c):

    if a+b>c and a+c>b and b+c>a :

        p=(a+c+b)/2

        s=math.sqrt(p*(p-a)*(p-b)*(p-c))

        return s

    else:

        return 0



main()





2.

employee_infos = []



def print_menu():

    print("=" * 30)

    print(" 员工管理系统 ")

    print("1.添加员工信息")

    print("2.删除员工信息")

    print("3.修改员工信息")

    print("4.显示所有员工信息")

    print("0.退出系统")

    print("=" * 30)



def add_info():

    new_name = input("请输入新员工的名字：")

    new_sex = input("请输入新员工的性别：(男/女)")

    new_infos = {}

    new_infos['name'] = new_name

    new_infos['sex'] = new_sex

    employee_infos.append(new_infos)





def del_info(employee):

    del_number = int(input("请输入要删除的序号：")) - 1

    del employee[del_number]





def modify_info():

    employee_id = int(input("请输入要修改的员工的序号："))

    new_name = input("请输入新员工的名字：")

    new_sex = input("请输入新员工的性别：(男/女)")

    employee_infos[employee_id - 1]['name'] = new_name

    employee_infos[employee_id - 1]['sex'] = new_sex





def show_infos():

    print("=" * 30)

    print("学生的信息如下:")

    print("=" * 30)

    print("序号    姓名    性别   ")

    i = 1

    for temp in employee_infos:

        print("%d      %s      %s" % (i, temp['name'], temp['sex']))

        i += 1





def main():

    while True:

        print_menu()        

        key = input("请输入功能对应的数字:") 

        if key == '1':    

            add_info()

        elif key == '2':  

            del_info(employee_infos)

        elif key == '3': 

            modify_info()

        elif key == '4': 

            show_infos()

        elif key == '0':  

            quit_confirm = input("亲，真的要退出么？(Yes or No):")

            if quit_confirm == "Yes":

                break    

            else:

                print("输入有误，请重新输入")





main()
