#coding:utf_8
'''
<ルジャンドル予想>
任意の自然数nについてn^2と(n+1)^2の間には必ず素数が存在する。
'''

from functions import primeNum

natureNum = input('n=')
print('n='+str(natureNum))
print('<<'+str(natureNum**2)+'〜'+str((natureNum+1)**2)+'>>')
num1 = natureNum**2+1
num2 = (natureNum+1)**2-1
i = 1
times = num2-num1+1
x = num1

while i <= times:
    ans = primeNum(x)
    print(ans)
    i+=1
    x+=1
