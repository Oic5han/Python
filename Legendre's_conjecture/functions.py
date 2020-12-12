#coding:utf_8

def primeNum(num):
    x = 1
    count = 0

    while x <= num:
        if num%x == 0:
            count += 1
        x += 1

    if count == 2:
        ans = str(num)+'：◯'
        return ans
    else:
        ans = str(num)+'：×'
        return ans
