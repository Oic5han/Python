#coding:utf_8
'''
<コラッツ予想>
どんな正の整数も
偶数→2で割る・奇数→3倍して1足す
という操作を繰り返すことで必ず1に到達する
'''

import functions

#初期値設定
baseNum = int(input('n='))
print(baseNum)

#条件操作を繰り返す
while baseNum!=1:
    baseNum = functions.collatz(baseNum)
    print(baseNum)
print('end')
