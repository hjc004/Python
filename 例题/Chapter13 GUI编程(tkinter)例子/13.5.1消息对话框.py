from tkinter.messagebox import *
from tkinter import *
top = Tk()
def hello():
    showinfo("Say Hello", "Hello World")
button = Button(top, text="Say Hello", command=hello)
button.pack()
top.mainloop()
