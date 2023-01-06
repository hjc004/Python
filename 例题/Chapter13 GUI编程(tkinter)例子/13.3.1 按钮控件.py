from tkinter import *
root = Tk()
def callback():
     print('学Python，可以搞大事')
button = Button(root,text='人生苦短，我用Python',command=callback)
button.pack()
root.mainloop()
