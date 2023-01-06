import time

try:
    file = open('test.txt', "w+")
    while True:
        content = file.read()
        if len(content) == 0:
            break
        time.sleep(2)
        print(content)
finally:
    file.close()
    print('关闭文件')



