#coding:utf_8

def collatz(num):
    if num%2==0:
        ans = num/2
    else:
        ans = num*3+1

    return ans
