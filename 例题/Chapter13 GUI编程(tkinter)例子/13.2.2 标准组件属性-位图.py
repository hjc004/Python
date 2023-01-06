from tkinter import *
top = Tk()
button_one = Button(top, text="error", relief=RAISED,
bitmap="error")
button_two = Button(top, text="gray75", relief=RAISED,
bitmap="gray75")
button_three = Button(top, text="gray75", relief=RAISED,
bitmap="gray75")
button_four = Button(top, text="gray25", relief=RAISED,
bitmap="gray25")
button_five = Button(top, text="gray12", relief=RAISED,
bitmap="gray12")
button_six = Button(top, text="hourglass", relief=RAISED,
bitmap="hourglass")
button_seven = Button(top, text="info", relief=RAISED,
                               bitmap="info")
button_eight = Button(top, text="questhead", relief=RAISED,
                               bitmap="questhead")
button_nine = Button(top, text="question", relief=RAISED,
                             bitmap="question")
button_ten = Button(top, text="warning", relief=RAISED,
                            bitmap="warning")
button_one.pack()
button_two.pack()
button_three.pack()
button_four.pack()
button_five.pack()
button_six.pack()
button_seven.pack()
button_eight.pack()
button_nine.pack()
button_ten.pack()
top.mainloop()
