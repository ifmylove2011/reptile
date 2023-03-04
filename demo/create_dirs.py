# -*- coding: utf-8 -*-

# 创建模板目录

import sys
import os
from time import sleep
from tqdm import tqdm
# 这里同样的，tqdm就是这个进度条最常用的一个方法
# 里面存一个可迭代对象
# for i in tqdm(range(100), nrows=3,ncols=20):
#     sleep(0.01)

DIR_SUB = ['img','log','model']

def create_dirs(root,dir_name):
    os.chdir(root)
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    os.chdir(dir_name)
    for d in DIR_SUB:
        if not os.path.exists(d):
            os.mkdir(d)
    os.makedirs(os.path.join(root,dir_name,DIR_SUB[0],'100_'+dir_name))

dir = sys.argv[1]
name = sys.argv[2]
create_dirs(dir,name)
