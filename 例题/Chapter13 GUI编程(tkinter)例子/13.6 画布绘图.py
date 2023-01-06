from tkinter import *
import math
root = Tk()
canvas = Canvas(root, width=200, height=100)
canvas.pack()
center_x = 100
center_y = 50
r = 50
points = [
    #左上点
    center_x - int(r * math.sin(2 * math.pi / 5)),
    center_y - int(r * math.cos(2 * math.pi / 5)),
        # 右上点
        center_x + int(r * math.sin(2 * math.pi / 5)),
        center_y - int(r * math.cos(2 * math.pi / 5)),
        # 左下点
        center_x - int(r * math.sin(math.pi / 5)),
        center_y + int(r * math.cos(math.pi / 5)),
        # 顶点
        center_x,
        center_y - r,
        # 右下点
        center_x + int(r * math.sin(math.pi / 5)),
        center_y + int(r * math.cos(math.pi / 5))
    ]
canvas.create_polygon(points, outline='red', fill='')
root.mainloop()
