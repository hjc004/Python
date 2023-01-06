# 星期一： Mon.=Monday 
# 星期二： Tues.=Tuesday 
# 星期三： Wed.=Wednesday 
# 星期四： Thur.=Thursday 
# 星期五： Fri.=Friday 
# 星期六： Sat.=Saturday 
# 星期天： Sun.=Sunday
# 首字母两个T两个S
while True:
    D = input('Please input the first word:')
    if D == 'M':
        print('Monday')
    elif D == 'W':
        print('Wednesday')
    elif D == 'F':
        print('Friday')
    elif D == 'S':
        K = input('plz input 2:')
        print('Saturday'if K == 'a'else 'Sunday')
    elif D == 'T':
        K = input('plz input 2:')
        print('Thursday 'if K == 'h'else 'Tuesday')
    elif D == 'q' or D == 'Q':
        print('程序结束！')
        exit()
    else:
        print('请输入正确的字母！')
