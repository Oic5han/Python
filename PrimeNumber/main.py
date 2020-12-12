#coding:utf_8

'''
ひたすら素数を求めるプログラム
'''


min = input('min=')
max = input('max=')

num = min
div = 1
count = 0

while num <= max:
    div = 1
    count = 0

    while div <= num:
        if num%div == 0:
            count += 1
        div += 1

    if count == 2:
        print(str(num)+'：◯')
    else:
        print(str(num)+'：×')

    num += 1
