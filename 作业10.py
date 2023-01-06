'''
1、写一个应用程序，主要是体现父类子类间的继承关系。父类：鸟，子类：麻雀、鸵鸟、
鹰。子类继承父类的一些特点，如都是鸟的话就都会有翅膀、两条腿等，但它们各自
又有各自的特点，如麻雀的年龄、体重；鸵鸟的身高、奔跑速度；鹰的捕食、飞翔高度等。
'''

lass Bird(object):

    def __init__(self,leg,wing):

        self.leg=leg

        self.wing=wing



class Sparrow(Bird):

    def __init__(self,leg,wing):

        self.age = "10年"

        self.weight = "0.05kg"

        super().__init__(leg,wing)



class Ostrich(Bird):

    def __init__(self,leg,wing):

        self.height = "280cm"

        self.speed= "72km/h"

        super().__init__(leg,wing)



class Eagle(Bird):

    def __init__(self,leg,wing):

        self.predation = "肉食"

        self.fly_height = "8800m"

        super().__init__(leg,wing)



animal1=Sparrow(2,2)

print('麻雀的寿命是：%s'%animal1.age)

print('麻雀的重量是：%s'%animal1.weight)

print('麻雀有%s只翅膀'%animal1.wing)

print('麻雀有%s只腿\n'%animal1.leg)



animal2=Ostrich(2,2)

print('鸵鸟的高度是：%s'%animal2.height)

print('鸵鸟的速度是：%s'%animal2.speed)

print('鸵鸟有%s只翅膀'%animal1.wing)

print('鸵鸟有%s只腿\n'%animal1.leg)



animal3=Eagle(2,2)

print('鹰的食性是：%s'%animal3.predation)

print('鹰的飞行高度是：%s'%animal3.fly_height)

print('鹰有%s只翅膀'%animal1.wing)

print('鹰有%s只腿\n'%animal1.leg)

