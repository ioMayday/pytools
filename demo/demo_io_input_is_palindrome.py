# -*- coding: utf-8 -*-
"""
Created on 240904
博客：Python世界：输入输出之回文串判别实践
地址：https://blog.csdn.net/qq_17256689/article/details/141939580
功能：判断是否回文字符串
1、支持中英文
2、支持强回文和非强回文模式切换
"""

import string                           # 引用英文标点符号
from zhon.hanzi import punctuation      # 引用中文标点符号


def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


def print_palindrome_check_result(is_palindrome):
    if is_palindrome == True:
        print("Yes, it is a palindrome")
    else:
        print("No, it is not a palindrome")


def check_palindrome_strict(strs):
    if is_palindrome(strs):
        print_palindrome_check_result(True)
    else:
        print_palindrome_check_result(False)


def rm_target_ch_in_source(strs, target):
    for ch in target:
        strs = strs.replace(ch, '')
    return strs


def check_palindrome_not_strict(strs):
    print(strs)
    strs = strs.lower() # 全小写
    strs = strs.replace(' ', '') # 空格替换

    punc_en = string.punctuation
    strs = rm_target_ch_in_source(strs, punc_en)

    punc_zh = punctuation
    strs = rm_target_ch_in_source(strs, punc_zh)

    print(strs)
    check_palindrome_strict(strs)
    return


def check_palindrome_proc(is_strict_palindrome):
    input_str = input("Enter text: ")

    # input_str = "madam"
    # input_str = "sir"
    # input_str = "Rise to vote, sir."
    # input_str = "你好，好你"
    # input_str = "你好，Y好你？?!!!"
    # input_str = "你，是，谁啊？"
    if is_strict_palindrome:
        check_palindrome_strict(input_str)
    else:
        check_palindrome_not_strict(input_str)


if __name__ == '__main__':
    print('start!')

    # 正式运行
    # is_strict_palindrome = True # 支持强回文模式
    is_strict_palindrome = False # 不支持强回文模式，忽略标点符号及大小写
    check_palindrome_proc(is_strict_palindrome)

    # 正式退出main函数进程，以免main函数空跑
    print('done!')

