from tkinter import *
from tkinter.filedialog import *
def callback():
    name = askopenfilename()
    print(name)
button = Button(text='File Open', command=callback)
button.pack()
mainloop()
