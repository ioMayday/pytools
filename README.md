# pytools
常用python脚本工具代码

结构：

- demo，存放一些小项目尝试，可供交流参考
- audio，存放音频相关脚本工具，可供外部调用
- utils，存放自用提效脚本工具，可供外部调用


TBD
- 拆分audio为param和db
    - calc_param
    - sp2db



## 工具函数集

----



### 文件名与目录处理

```python
import os

# 获取当前目录下所有文件名列表，不含绝对路径
def get_dir_files_name(dir_in):
    files_name = os.listdir(dir_in)
    return files_name


# 获取当前目录下所有文件对应的绝对路径，dir_in下面不能包含子目录
def get_dir_files_path(dir_in):
    files_path = []
    for (dirpath, dirnames, filenames) in os.walk(dir_in):
        for filename in filenames:
            files_path += [os.path.join(dirpath, filename)]
    files_path.sort()
    return files_path


# 分离文件绝对路径的目录和文件名
def get_file_dir_and_name(file_path):
    head_tail = os.path.split(file_path)
    file_dir = head_tail[0]
    file_name = head_tail[1]
    return file_dir, file_name
```

## 文本文件处理

```python
# 获取文本文件中的文件路径列表
def get_txt_namelist(txt_path):
    f = open(txt_path,'r')    # 打开文件
    name_list = f.readlines()
    return name_list


# 将List数据输出到文本文件中
def print_list_to_txt(str_list, file_path):
    f = open(file_path, 'w+', encoding='utf-8')
    for item in str_list:
        nums = len(item)
        if nums < 3:
            continue
        # 每行输出格式控制
        out_str = 'ref: {}, out: {}, odg: {}\n'.format(item[0], item[1], item[2])
        f.write(out_str)
    f.close()
    return
```
