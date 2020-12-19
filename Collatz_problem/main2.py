#coding:utf_8
'''
<コラッツ予想>
どんな正の整数も
偶数→2で割る・奇数→3倍して1足す
という操作を繰り返すことで必ず1に到達する
'''

import functions

min = int(input('min='))
max = int(input('man='))

for num in range(min, max+1):
    print(num)
    while num!=1:
        num = functions.collatz(num)
        print(num)
    print('end\n')
