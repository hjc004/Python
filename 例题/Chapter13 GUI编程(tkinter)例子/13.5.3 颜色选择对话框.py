from tkinter import *
from tkinter.colorchooser import *
def callback():
    result = askcolor(color="#6A9662", title = "请选择一种您喜欢的颜色")
    print(result)
root = Tk()
button = Button(root, text='请选择一种颜色', command=callback)
button.pack()
mainloop()
