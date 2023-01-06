from tkinter import *
top = Tk()
button_one = Button(top, text ="circle", relief=RAISED, cursor="circle")
button_two = Button(top, text ="plus", relief=RAISED, cursor="plus")
button_three = Button(top, text ="clock", relief=RAISED, cursor="clock")
button_one.pack()
button_two.pack()
button_three.pack()
top.mainloop()
