from tkinter import *   #导入模块
root = Tk()
root.title("顶层窗口")   #创建顶层窗口

f1 = Frame(root)     #定义框架
label = Label(root, text="1 + 1 = ?")
e1 = StringVar()
Entry(f1, width = 50, textvariable = e1).pack(side = LEFT)  #基本输入框
#e1.set('请输入答案')
label.pack()
f1.pack()

root.mainloop()
