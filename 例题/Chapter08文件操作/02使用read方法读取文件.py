file = open('itheima.txt', 'r')
content = file.read(12)
print(content)
print("-" * 30)
content = file.read()
print(content)
file.close()
