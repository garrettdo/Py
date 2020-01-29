# 请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
#
# 程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。


letter = input('Please input:')
if letter == 'S':
    print('Please input second letter:')
    letter = input('Please input:')
    if letter == 'a':
        print('Saturday')
    elif letter == 'u':
        print('Sunday')
    else:
        print('Date error')

elif letter == 'F':
    print('Friday')
elif letter == 'M':
    print('Monday')
elif letter == 'T':
    print('Please input second letter')
    letter = input('Please input:')
    if letter == 'u':
        print('Tuesday')
    elif letter == 'h':
        print('Thursday')
    else:
        print('Date error')

elif letter == 'W':
    print('Wednesday')
else:
    print('Date error')