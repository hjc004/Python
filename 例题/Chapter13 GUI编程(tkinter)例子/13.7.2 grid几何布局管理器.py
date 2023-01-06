from tkinter import *
root = Tk()
Label(root, text="First").grid(row=0)    # 位于第1行的标签组件
Label(root, text="Second").grid(row=1)   # 位于第2行的标签组件
entry_one = Entry(root)
entry_two = Entry(root)
button = Button(root, text='计算', height=2)  # 按钮的高度占据两行
button.grid(row=0, column=2, rowspan=2)   # 按钮位于第1行第2列，且跨2行
entry_one.grid(row=0, column=1) # 位于第1行，第2列的文本框
entry_two.grid(row=1, column=1) # 位于第2行，第2列的文本框
root.mainloop()
