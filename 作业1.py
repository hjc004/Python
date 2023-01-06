'''
1．修改 chaos 程序（P10），让打印值的数量由用户确定。

a、获取另一个值代码：

N = eval(input(“How many numbers should I print? “))

b、需要更改循环参数，使用 n 代替具体的数字。



2、编写一个程序，将温度从华氏温度转换为摄氏温度。
'''

1、

def main():

     print("This program illustrates a chaotic function")

     x = eval(input("Enter a number between 0 and 1: "))

     n = eval(input("How many numbers should I print? "))

     for i in range(n):

         x = 3.9 * x * (1 - x)

         print(x)

 main()

 2、



def main():

    print("This program converts a temperature in Fahrenheit to a temperature in Celsius.")

    fahrenheit = eval(input("What is the Fahrenheit temperature? "))

    celsius = (fahrenheit - 32) * 5/9

    

    print("The temperature is", celsius, "degrees Celsius.")

    

main()

