#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()

# todo 使用模块的第一步，就是导入该模块
#  import 模块，然后可以用这个变量，就可以访问该模块的所有功能

# todo sys模块有一个argv变量，用list存储了   【命令行】 的所有参数。
#  argv至少有一个元素，因为第一个参数永远是该.py文件的名称，例如：
#  运行python3 hello.py获得的sys.argv就是['hello.py']；
#  运行python3 hello.py Michael获得的sys.argv就是['hello.py', 'Michael']。

#  if __name__=='__main__':
#     test()

# 在运行hello 模块的时候，py解释器将特殊变量__name__变为__main__
# 如果在其他地方导入该hello模块时，if判断将失败
# 因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试,测试模块内的方法

