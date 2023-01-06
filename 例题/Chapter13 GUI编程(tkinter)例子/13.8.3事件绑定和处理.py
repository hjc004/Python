from tkinter import *
from tkinter.messagebox import *
def handler(event):
    showinfo("点到了",'你好！')
root = Tk()
button = Button(root, text='点我呀')
button.bind('<Button-1>', handler)
button.pack()
root.mainloop()
