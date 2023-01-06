# 计算1~num的累积和
def calculate(number):
    result = 0
    i = 1
    while i <= number:
        result = result + i
        i += 1
    return result
result = calculate(100)
print('1~100的累积和为:', result)