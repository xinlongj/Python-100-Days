"""
找出100~999之间的所有水仙花数
水仙花数是各位立方和等于这个数本身的数
如: 153 = 1**3 + 5**3 + 3**3

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""

for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)


for i in range(100, 1000, 1):
    high = i // 100
    mid = i //100 % 10
    low = i % 10
    if i == high ** 3 + mid ** 3 + low ** 3:
        print('%d is lily number' % i)
