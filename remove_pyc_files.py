# coding=utf-8
'''
Created on 2018年8月16日

@author: xiangmingzhe
'''
import os
path = 'D:\Git\Chuan_Interface_Django'   #项目的绝对路径
for prefix, dirs, files in os.walk(path):
    for name in files:
        if name.endswith('.pyc'):
            filename = os.path.join(prefix, name)
            os.remove(filename)
print("Clear Up!")