from tkinter import *
top = Tk()
label = Label(top, text="User Name")
label.pack(side=LEFT)
entry = Entry(top, bd=5)
entry.pack(side=RIGHT)
top.mainloop()
