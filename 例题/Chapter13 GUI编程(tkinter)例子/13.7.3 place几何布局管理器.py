from tkinter import *
from tkinter.messagebox import *
root = Tk()
def hello_call_back():
      showinfo( "Hello Python", "Hello World")
button = Button(root, text="Hello", command=hello_call_back)
button.pack()
button.place(relx=0.5, rely=0.5, anchor=CENTER)
root.mainloop()
