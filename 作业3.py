'''
1、 P51题15  编写程序，通过对这个级数的项进行求和来求近似的 π 值：
4/1 – 4/3 + 4/5 – 4/7 + 4/9 − 4/11 + ……
程序应该提示用户输入 n，要求和的项数，然后输出该级数的前n 个项的和。
让你的程序从math.pi 的值中减去近似值，看看它的准确性。

2、P51题 16斐波那契序列是数字序列，其中每个连续数字是前两个数字的和。
经典的斐波那契序列开始于 1，1，2，3，5，8，13，……。
编写计算第n 个斐波纳契数的程序，其中 n 是用户输入的值。
例如，如果 n = 6，则结果为 8。
'''

P51题15  编写程序，通过对这个级数的项进行求和来求近似的 π 值：4/1 – 4/3 + 4/5 – 4/7 + 4/9 − 4/11 + …… 程序应该提示用户输入 n，要求和的项数，然后输出该级数的前n 个项的和。让你的程序从math.pi 的值中减去近似值，看看它的准确性。
 
#   A program to approximate the value of pi by summing the terms
#   of this series: 4/1 - 4/3 + 4/5 = 4/7 + 4/9 - 4/11 + ...
import math
def main():
    estimate = 0
    n = int(input("Please enter the number of terms to sum: "))
    for k in range(1, n + 1):
        estimate += (-1) ** (k + 1) * 4 / (2 * k - 1)
    error = abs(math.pi - estimate)
    print("""The approximation of pi is {0}, which is {1}
    away from the value of math.pi({2})""".format(estimate, error, math.pi))

main()
# Output:
# Please enter the number of terms to sum: 10000000
# The approximation of pi is 3.1415925535897915, which is 1.0000000161269895e-07
#     away from the value of math.pi(3.141592653589793)
 
 
P51题 16斐波那契序列是数字序列，其中每个连续数字是前两个数字的和。经典的斐波那契序列开始于 1，1，2，3，5，8，13，……。编写计算第n 个斐波纳契数的程序，其中 n 是用户输入的值。例如，如果 n = 6，则结果为 8。
 
#   A program to compute the nth Fibonacci number where n is a value input by the user
def fibonacci(n):
    if n <= 0:
        raise ValueError("n must be positive")
    elif n < 2:
        return n
    fib_n_minus_one = 1
    fib_n_minus_two = 0
    fib_n = 0
    for _ in range(2, n + 1):
        fib_n = fib_n_minus_one + fib_n_minus_two
        fib_n_minus_two = fib_n_minus_one
        fib_n_minus_one = fib_n
    return fib_n

def main():
    n = int(input("n = "))
    fib_n = fibonacci(n)
    print("The {0}th Fibonacci number is {1}".format(n, fib_n))

main()
 
