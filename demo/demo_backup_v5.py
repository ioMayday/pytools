# -*- coding: utf-8 -*-
'''
博客：Python世界：文件自动化备份实践
地址：https://blog.csdn.net/qq_17256689/article/details/141871169
'''


d# -*- coding: utf-8 -*-
"""
Created on 09/03/24
功能：文件备份
1、指定待备份目录和目标备份路径
2、按日期建立文件夹
3、按时间建立压缩文件
"""

import os
import time
import sys
import zipfile


# 判断该目录是否存在，如不存在，则创建
def if_not_exist_then_mkdir(path_in):
    if not os.path.exists(path_in):
        os.mkdir(path_in)
        print("Successfully created directory", path_in)


# 仅支持单个目录备份
def backup_proc(tobe_backup_dir, target_dir, comment_info):
    if_not_exist_then_mkdir(target_dir)
    today = target_dir + os.sep + "backup_" + time.strftime("%Y%m%d") # 年、月、日
    now = time.strftime("%H%M%S") # 小时、分钟、秒
    print("Successfully created")

    # zip命名及目录处理
    prefix = today + os.sep + now
    if len(comment_info) == 0:
        target = prefix + '.zip'
    else:
        target = prefix + "_" + comment_info.replace(" ", "_") + '.zip'
    if_not_exist_then_mkdir(today)

    # 参考链接：https://blog.csdn.net/csrh131/article/details/107895772
    # zipfile打开文件句柄, with打开不用手动关闭
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as f:
        for root_dir, dir_list, file_list in os.walk(tobe_backup_dir): # 能遍历子目录所有文件
            for name in file_list:
                target_file = os.path.join(root_dir, name)
                all_file_direct_zip = False
                if all_file_direct_zip: # 不加内部目录
                    zip_internal_dir_prefix = os.sep
                else: # 加内部目录
                    zip_internal_dir_prefix = comment_info + os.sep
                # 去掉绝对路径指定压缩包里面的文件所在目录结构   
                arcname = zip_internal_dir_prefix + target_file.replace(tobe_backup_dir, "")
                # arcname = target_file.replace(tobe_backup_dir, "")
                f.write(target_file, arcname=arcname)
    return


if __name__ == '__main__':
    print('start!')

    # 前处理
    if len(sys.argv) >= 3: # 有外部入参，取外部输入
        tobe_backup_dir = sys.argv[1] # input dir, sys.argv[0] the name of python file
        target_dir = sys.argv[2] # output dir
        comment_info = input("enter a comment information => ")
    else: # 无外部入参，则内部设定
        # tobe_backup_dir = "C:\\Users\\other"
        tobe_backup_dir = r"E:\roma_data\code_data_in\inbox"
        target_dir = "E:\\roma_data\\code_test"
        comment_info = "test demo"

    # 正式运行
    backup_proc(tobe_backup_dir, target_dir, comment_info)

    # 正式退出main函数进程，以免main函数空跑
    print('done!')
    sys.exit()


