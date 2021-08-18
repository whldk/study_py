# coding:utf-8

import os


# 获取当前的路径
curr = os.getcwd()


print(curr)

# 获取当前的目录
data = os.listdir(curr)

print(data)

# 创建目录

new_path = '%s/test2/abc' % curr
os.mkdir(new_path)


