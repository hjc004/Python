from tkinter import *
root = Tk()
button_one = Button(text='按钮1')
button_one.pack(side=LEFT)
button_two = Button(text='按钮2')
button_two.pack(side=RIGHT)
button_three = Button(text='按钮3')
button_three.pack(side=TOP)
button_four = Button(text='按钮4')
button_four.pack(side=BOTTOM)
root.mainloop()
