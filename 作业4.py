'''
1､ 输入星期几的第一个字母，用来判断是星期几，如果第一个字母一样，
则继续判断第二个字母，以此类推。

2、编写一个可以编码和解码凯撒密码的程序。
（要求：凯撒密码是一种简单的替换密码，其思路是将明文消息的每个字母在字母表中
移动固定数字（称为密钥）。例如，如果键值为 2，则单词“Sourpuss”将被编码为
“Uqwtrwuu”。原始消息可以通过使用密钥的负值“重新编码”来恢复。对程序的输入
将是明文的字符串和密钥的值。输出将是一个编码消息，其中原始消息中的每个字符都
将被替换为 Unicode 字符集中后移密钥个字符。例如，如果ch 是字符串中的字符，
key 是要移位的量，则替换 ch 的字符可以计算为 chr（ord（ch）+ key））
'''

 1、

week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

while True:

    myStr = input("请输入任意一个字母:")

    upMyStr = myStr.upper()

    for weekS in week:

        if upMyStr == weekS[0]:

            if weekS.startswith("M"):

                print("星期一")

            elif weekS.startswith("W"):

                print("星期三")

            elif weekS.startswith("F"):

                print("星期五")

            elif weekS.startswith("T") or weekS.startswith("S"):

                secondStr = input("请再输入任意一个字母:")

                newStr = upMyStr+secondStr

                print(newStr)

                for weekStr in week:

                    if weekStr.find(newStr,0,2) != -1:

                        if newStr == "Tu":

                            print("星期二")

                        elif newStr == "Th":

                            print("星期四")

                        elif newStr == "Sa":

                            print("星期六")

                        elif newStr == "Su":

                            print("星期日")

                        break

            break



2、

# c05ex06.py

#     Numerology of a full name





def main():

    print("This program computes the 'number value' of a name")

    print()



    names = input("Enter a name: ")



    # Create a string of all the letters -- avoids nested loop

    letters = "".join(names.split())

    total = 0

    for letter in letters:

        total = total + ord(letter.lower()) - ord('a') + 1



    print("The value is:", total)



main()



