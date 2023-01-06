'''
1、 已知学校管理应用程序，有学生和教师，请编写多个函数：增加、删除、修改和
查询的学生和教师信息。和学生的成绩管理。

   a.要有权限设计,有帐号和密码。通过修饰器完成。
   b.要有菜单的设计。
   c.数据保存在文件里。
'''

student_infos = []

teacher_infos = []

student_score = []



def access(func):

    def inner():

        print("欢迎进入管理系统V1.0")

        ac = input("请输入教师账号: ")

        pw = input("请输入教师密码: ")

        if ac == "123" and pw == "123":

            func()

        else:

            print("账号密码错误")

            main()

    return inner



# 打印功能提示

def print_menu():

    print("=" * 30)

    print("1.进入学生管理系统")

    print("2.进入教师管理系统")

    print("3.保存数据")

    print("0.退出")

    print("=" * 30)



def print_stu_menu():

    while True:

        print("=" * 30)

        print("1.添加学生信息")

        print("2.删除学生信息")

        print("3.修改学生信息")

        print("4.显示学生信息")

        print("5.学生成绩添加")

        print("6.查看学生成绩")

        print("7.学生成绩保存")

        print("0.退出学生系统")

        print("=" * 30)

        key = input("请输入功能对应的数字:")  # 获得用户输入的序号

        if key == '1':  # 添加学生的信息

            add_info(student_infos)

        elif key == '2':  # 删除学生的信息

            del_info(student_infos)

        elif key == '3':  # 修改学生的信息

            modify_info(student_infos)

        elif key == '4':  # 修改学生的信息

            show_infos(student_infos)

        elif key == '5':  # 添加学生成绩

            add_score()

        elif key == '6':  # 查看学生成绩

            show_score()

        elif key == '7':  # 保存学生成绩

            save_score()

        elif key == '0':  # 退出

            break

        else:

            print("输入有误，请重新输入")



def print_tea_menu():

    while True:

        print("=" * 30)

        print("1.添加教师信息")

        print("2.删除教师信息")

        print("3.修改教师信息")

        print("4.显示教师信息")

        print("0.退出教师系统")

        print("=" * 30)

        key = input("请输入功能对应的数字:")  # 获得用户输入的序号

        if key == '1':  # 添加学生的信息

            add_info(teacher_infos)

        elif key == '2':  # 删除学生的信息

            del_info(teacher_infos)

        elif key == '3':  # 修改学生的信息

            modify_info(teacher_infos)

        elif key == '4':  # 查看所有学生的信息

            show_infos(teacher_infos)

        elif key == '0':  # 退出

            break

        else:

            print("输入有误，请重新输入")



# 添加信息

def add_info(stuOrTea_infos):

    # 提示并获取的姓名

    new_name = input("请输入的名字：")

    # 提示并获取的性别

    new_sex = input("请输入的性别：(B/G)")

    # 提示并获取的手机号码

    new_phone = input("请输入的手机号码：")

    new_infos = {}

    new_infos['name'] = new_name

    new_infos['sex'] = new_sex

    new_infos['phone'] = new_phone

    stuOrTea_infos.append(new_infos)



def add_score():

    new_num = input("请输入的学号：")

    new_score = input("请输入成绩：")

    score = {}

    score['num'] = new_num

    score['score'] = new_score

    student_score.append(score)



# 删除信息

def del_info(stuOrTea_infos):

    del_number = int(input("请输入要删除的序号：")) - 1

    del stuOrTea_infos[del_number]



# 修改信息

def modify_info(stuOrTea_infos):

    id = int(input("请输入要修改的学生的序号："))

    new_name = input("请输入新的名字：")

    new_sex = input("请输入新的性别：(男/女)")

    new_phone = input("请输入新的手机号码：")

    stuOrTea_infos[id - 1]['name'] = new_name

    stuOrTea_infos[id - 1]['sex'] = new_sex

    stuOrTea_infos[id - 1]['phone'] = new_phone



# 定义一个用于显示所有信息的函数

def show_infos(stuOrTea_infos):

    print("=" * 30)

    print("信息如下:")

    print("=" * 30)

    print("序号    姓名    性别   手机号码")

    i = 1

    for temp in stuOrTea_infos:

        print("%d      %s      %s     %s" % (i, temp['name'], temp['sex'], temp['phone']))

        i += 1



def show_score():

    print("=" * 30)

    print("信息如下:")

    print("=" * 30)

    print("学号    成绩")

    i = 1

    for temp in student_score:

        print("%s      %s" % (temp['num'], temp['score']))

        i += 1



def save_to_file():

    file = open("backup.data", "w")

    file.write("学生信息: \n")

    for i in student_infos:

        file.write(str(i) + "\n")

    file.write("教师信息: \n")

    for i in teacher_infos:

        file.write(str(i) + "\n")

    file.close()



def save_score():

    file = open("score.data", "w")

    file.write("学生成绩: \n")

    for i in student_score:

        file.write(str(i) + "\n")

            

@access

def main():

    while True:

        print_menu()        # 打印菜单

        key = input("请输入功能对应的数字:")  # 获得用户输入的序号

        if key == '1':     # 进入学生管理系统

            print_stu_menu()

        elif key == '2':  # 删除学生的信息

            print_tea_menu()

        elif key == '3':  # 保存文件

            save_to_file()

            print("数据保存成功")

        elif key == '0':  # 退出系统

            quit_confirm = input("亲，真的要退出么？(Yes or No):")

            if quit_confirm == "Yes":

                break

            else:

                print("输入有误，请重新输入")



main()
