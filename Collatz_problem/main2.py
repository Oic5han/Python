#coding:utf_8
'''
<コラッツ予想>
どんな正の整数も
偶数→2で割る・奇数→3倍して1足す
という操作を繰り返すことで必ず1に到達する
'''

import functions

#複数の数字で計算する
for num in range(1, 51):
    print(num)
    #条件操作を繰り返す
    while num!=1:
        x = functions.collatz(num)
        num = x
        print(int(num))
    print('end\n')
