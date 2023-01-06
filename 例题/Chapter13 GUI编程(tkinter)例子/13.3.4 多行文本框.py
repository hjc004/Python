from tkinter import *
root = Tk()
label = Label(root, text='请写下您的意见或者建议')
label.pack()
text = Text(root, width=30, height=5, bg='yellow', highlightbackground='red')
text.pack()
root.mainloop()
