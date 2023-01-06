from tkinter import *
def sel():
 	selection = "You selected the option " + str(var.get())
 	label.config(text=selection)
root = Tk()
var = IntVar()
radio_button_one = Radiobutton(root, text="Option 1", variable=var,
value=1, command=sel)
radio_button_one.pack()
radio_button_two = Radiobutton(root, text="Option 2", variable=var,
value=2, command=sel)
radio_button_two.pack()
radio_button_three = Radiobutton(root, text="Option 3", variable=var,
value=3, command=sel)
radio_button_three.pack()
label = Label(root)
label.pack()
root.mainloop()
