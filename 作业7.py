'''
1、 已知学校管理应用程序，有学生和教师，请编写多个函数：增加、删除、修改和查询
的学生和教师信息。

   a.要有权限设计,有帐号和密码。通过修饰器完成。
   b.要有菜单的设计。

（菜单用例：）
# 用来保存学生的所有信息
student_infos = []

# 打印功能提示
def print_menu():
    print("=" * 30)
    print(" 学生管理系统V1.0 ")
    print("1.添加学生信息")
    print("2.删除学生信息")
    print("3.修改学生信息")
    print("4.显示所有学生信息")
    print("0.退出系统")
    print("=" * 30)

# 添加一个学生信息
def add_info():

    # 提示并获取学生的姓名
    new_name = input("请输入新学生的名字：")

    # 提示并获取学生的性别
    new_sex = input("请输入新学生的性别：(男/女)")

    # 提示并获取学生的手机号码
    new_phone = input("请输入新学生的手机号码：")
    new_infos = {}
    new_infos['name'] = new_name
    new_infos['sex'] = new_sex
    new_infos['phone'] = new_phone
    student_infos.append(new_infos)

# 删除一个学生信息
def del_info(student):
    del_number = int(input("请输入要删除的序号：")) - 1
    del student[del_number]

# 修改一个学生的信息
def modify_info():
    student_id = int(input("请输入要修改的学生的序号："))
    new_name = input("请输入新学生的名字：")
    new_sex = input("请输入新学生的性别：(男/女)")
    new_phone = input("请输入新学生的手机号码：")
    student_infos[student_id - 1]['name'] = new_name
    student_infos[student_id - 1]['sex'] = new_sex
    student_infos[student_id - 1]['phone'] = new_phone

# 定义一个用于显示所有学生信息的函数
def show_infos():
    print("=" * 30)
    print("学生的信息如下:")
    print("=" * 30)
    print("序号    姓名    性别   手机号码")
    i = 1
    for temp in student_infos:
        print("%d      %s      %s     %s" % (i, temp['name'], temp['sex'], temp['phone']))
        i += 1

def main():
    while True:
        print_menu()        # 打印菜单
        key = input("请输入功能对应的数字:")  # 获得用户输入的序号
        if key == '1':     # 添加学生的信息
            add_info()
        elif key == '2':  # 删除学生的信息
            del_info(student_infos)
        elif key == '3':  # 修改学生的信息
            modify_info()
        elif key == '4':  # 查看所有学生的信息
            show_infos()
        elif key == '0':  # 退出系统
            quit_confirm = input("亲，真的要退出么？(Yes or No):")
            if quit_confirm == "Yes":
                break      # 结束循环
            else:
                print("输入有误，请重新输入")
                
main()
'''

# 用来保存学生的所有信息

student_infos = []

# 用来保存教师的所有信息

teacher_infos = []

#登录密码和账号

admin_infos = {'admin':'bnuz','code':'zhuhai'}



#登录功能

def login_confirm(func):

    def inner():

        while True:

            print("请输入账户和密码：")

            account=input("账号：")

            keys=input("密码：")

            if admin_infos['admin']==account and admin_infos['code']==keys:

                print("登陆成功!!!")

                func()

                break

            else:

                print("账户或密码错误!!!")

    return inner

    

 # 打印功能提示



def print_student_menu():

    print("=" * 30)

    print(" 学生管理系统V1.0 ")

    print("1.添加学生信息")

    print("2.删除学生信息")

    print("3.修改学生信息")

    print("4.显示所有学生信息")

    print("0.退出系统")

    print("=" * 30)

    

def print_teacher_menu():

    print("=" * 30)

    print(" 教师管理系统V1.0 ")

    print("1.添加教师信息")

    print("2.删除教师信息")

    print("3.修改教师信息")

    print("4.显示所有教师信息")

    print("0.退出系统")

    print("=" * 30)

    

# 添加一个教师信息

def add_teacher_info():

    # 提示并获取学生的姓名

    new_name = input("请输入新教师的名字：")

    # 提示并获取学生的性别

    new_sex = input("请输入新教师的性别：(男/女)")

    # 提示并获取学生的手机号码

    new_phone = input("请输入新教师的手机号码：")

    new_infos ={}

    new_infos['name'] = new_name

    new_infos['sex'] = new_sex

    new_infos['phone'] = new_phone

    teacher_infos.append(new_infos)



# 添加一个学生信息

def add_student_info():

    # 提示并获取学生的姓名

    new_name = input("请输入新学生的名字：")



    # 提示并获取学生的性别

    new_sex = input("请输入新学生的性别：(男/女)")



    # 提示并获取学生的手机号码

    new_phone = input("请输入新学生的手机号码：")

    new_infos = {}

    new_infos['name'] = new_name

    new_infos['sex'] = new_sex

    new_infos['phone'] = new_phone

    student_infos.append(new_infos)

# 删除一个教师信息

def del_teacher_info(teacher):

    del_number = int(input("请输入要删除的序号：")) - 1

    del tercher[del_number]

    

# 删除一个学生信息

def del_student_info(student):

    del_number = int(input("请输入要删除的序号：")) - 1

    del student[del_number]



# 修改一个教师的信息

def modify_teacher_info():

    teacher_id = int(input("请输入要修改的教师的序号："))

    new_name = input("请输入新教师的名字：")

    new_sex = input("请输入新教师的性别：(男/女)")

    new_phone = input("请输入新教师的手机号码：")

    teacher_infos[teacher_id - 1]['name'] = new_name

    teacher_infos[teacher_id - 1]['sex'] = new_sex

    teacher_infos[teacher_id - 1]['phone'] = new_phone

    

# 修改一个学生的信息

def modify_student_info():

    student_id = int(input("请输入要修改的学生的序号："))

    new_name = input("请输入新学生的名字：")

    new_sex = input("请输入新学生的性别：(男/女)")

    new_phone = input("请输入新学生的手机号码：")

    student_infos[student_id - 1]['name'] = new_name

    student_infos[student_id - 1]['sex'] = new_sex

    student_infos[student_id - 1]['phone'] = new_phone



# 定义一个用于显示所有教师信息的函数

def show_teacher_infos():

    print("=" * 30)

    print("教师的信息如下:")

    print("=" * 30)

    print("序号    姓名    性别   手机号码")

    i = 1



    for temp in teacher_infos:

        print("%d      %s      %s     %s" % (i, temp['name'], temp['sex'], temp['phone']))

        i += 1



# 定义一个用于显示所有学生信息的函数

def show_student_infos():

    print("=" * 30)

    print("学生的信息如下:")

    print("=" * 30)

    print("序号    姓名    性别   手机号码")

    i = 1

    for temp in student_infos:

        print("%d      %s      %s     %s" % (i, temp['name'], temp['sex'], temp['phone']))

        i += 1

        

@login_confirm       

def main():

    print("选择1.教师,2.学生")

    select = input("输入序号")

    if select == '1':

        while True:

            print_teacher_menu()       # 打印菜单

            key = input("请输入功能对应的数字:")  # 获得用户输入的序号

            if key == '1':     # 添加教师的信息

                add_teacher_info()

            elif key == '2':  # 删除教师的信息

                del_teacher_info(teacher_infos)

            elif key == '3':  # 修改教师的信息

                modify_teacher_info()

            elif key == '4':  # 查看所有教师的信息

                show_teacher_infos()

            elif key == '0':  # 退出系统

                quit_confirm = input("亲，真的要退出么？(Yes or No):")

                if quit_confirm == "Yes":

                    break      # 结束循环

            else:

                print("输入有误，请重新输入")

    else:

        while True:

            print_student_menu()        # 打印菜单

            key = input("请输入功能对应的数字:")  # 获得用户输入的序号

            if key == '1':     # 添加学生的信息

                add_student_info()

            elif key == '2':  # 删除学生的信息

                del_student_info(student_infos)

            elif key == '3':  # 修改学生的信息

                modify_student_info()

            elif key == '4':  # 查看所有学生的信息

                show_student_infos()

            elif key == '0':  # 退出系统

                quit_confirm = input("亲，真的要退出么？(Yes or No):")

                if quit_confirm == "Yes":

                     break      # 结束循环

            else:

                print("输入有误，请重新输入")





main()
