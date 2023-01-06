from tkinter import *
root = Tk()
menu = Menu(root)
for item in ['复制', '粘贴']:
    menu.add_command(label=item)
def pop(event):
    menu.post(event.x_root, event.y_root)
root.bind('<Button-3>', pop)
root.mainloop()
