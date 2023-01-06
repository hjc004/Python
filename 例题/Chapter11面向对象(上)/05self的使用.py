# 定义类
class Dog:
    def __init__(self, new_color):
        self.color = new_color

    def print_color(self):
        print("颜色为：%s" % self.color)


dog_white = Dog("白色")
dog_white.print_color()
dog_black = Dog("黑色")
dog_black.print_color()
