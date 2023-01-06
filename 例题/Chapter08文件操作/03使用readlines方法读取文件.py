file = open('itheima.txt', 'r')
content = file.readlines()
i = 1
for temp in content:
    print("%d:%s" % (i, temp))
    i += 1
file.close()
