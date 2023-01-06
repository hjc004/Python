from tkinter import *
top = Tk()
menu = Menu(top)
def callback():
 	print('this is menu')
for item in ['文件', '编辑', '视图', '格式']:
    menu.add_command(label=item, command=callback)
top['menu'] = menu
top.mainloop()
