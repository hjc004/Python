'''
1、假设你有一个投资计划，每年投资一定的固定金额。修改 futval.py（P30），
计算你的投资的总累积值。该程序的输入值是每年投资的金额、利率和投资的年数。
（P34题7）

2、 编写一个交互式 Python 计算器程序。程序应该允许用户键入数学表达式，然后打印表
达式的值。加入循环，以便用户可以执行许多次计算（例如，最多 100 个）。
（注意：要设计程序的退出）（P34题11）
'''

1:

# futval.py

def main():

    print("This program calculates the future value")

    print("of a n-year investment.")

    principal = eval(input("Enter the initial principal: "))

    apr = eval(input("Enter the annual interest rate: "))

    n = eval(input("Enter the years;"))

    for i in range(n):

        principal = principal * (1 + apr)

    print("The value in n years is:",principal)

main()

2:

def main():

    print("This program is an interactive calculator. Enter your calculations below.")



    for i in range(100):

        expression = eval(input(""))

        print(expression)



main()

