# -*- coding: utf-8 -*-
'''
博客：Python世界：求解满足某完全平方关系的整数实践
地址：https://blog.csdn.net/qq_17256689/article/details/141965909
'''

# -*- coding: utf-8 -*-
"""
功能：求例3的x值
1、初步分析限定范围
2、限定整数范围内遍历求解
"""

def find_x():
    x = []

    # i, j is even
    upper_bound = 168 // 2 + 1 # 加1目的是因为range左开右闭
    for i in range(2, upper_bound, 2):
        j = 168 // i # `//` 实现整数除法
        if j % 2 == 0:
            is_even = True
        else:
            is_even = False
        if i < j and i * j == 168 and is_even: # i, j地位等价，i>j时只是位置交换，x结果不变，故没必要遍历
            res = int(((i + j) / 2) ** 2 - 268)
            x.append(res)
    return x


if __name__ == '__main__':
    print('start!')

    # 正式运行
    x = find_x()
    print(x)

    # 正式退出main函数进程，以免main函数空跑
    print('done!')

