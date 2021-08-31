"""
定义和使用列表
- 用下标访问元素
- 添加元素
- 删除元素

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def main():
    fruits = ['grape', '@pple', 'strawberry', 'waxberry']
    print(fruits)
    # 通过下标访问元素
    print('fruits[0] = ' + fruits[0])
    print('fruits[1] = ' + fruits[1])
    print('fruits[-1] = ' + fruits[-1])
    print('fruits[-2] = ' + fruits[-2])
    # print(fruits[-5]) # IndexError
    # print(fruits[4])  # IndexError
    fruits[1] = 'apple'
    print(fruits)
    # 添加元素
    fruits.append('pitaya')
    fruits.insert(0, 'banana')
    print(fruits)
    # 删除元素
    print('开始删除')
    del fruits[1]
    print(fruits)
    fruits.pop()
    print(fruits)
    fruits.pop(0)
    print(fruits)
    fruits.remove('apple')
    print(fruits)

if __name__ == '__main__':
    main()
