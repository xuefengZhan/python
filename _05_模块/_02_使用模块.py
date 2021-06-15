#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

#todo 说明：
# 第1行和第2行是标准注释，
# 第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行
# 第2行注释表示.py文件本身使用标准UTF-8编码；
# 第4行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
# 第6行使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；
# 以上就是Python模块的标准文件模板，当然也可以全部删掉不写，但是，按标准办事肯定没错。

# 接下来就是真正的代码部分
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

#  todo 1.使用模块的第一步，就是导入该模块
#  import 模块，然后可以通过这个变量可以访问该模块的所有功能

#  todo sys模块有一个argv变量，用list存储了   【命令行】的所有参数。
#  argv至少有一个元素，因为第一个参数永远是该.py文件的名称，例如：
#  运行python3 hello.py获得的sys.argv就是['hello.py']；
#  运行python3 hello.py Michael获得的sys.argv就是['hello.py', 'Michael']。

# todo
#  if __name__=='__main__':
#     test()

# 1. __name__的理解1.1 为什么使用__name__属性？
# Python解释器在导入模块时，会将模块中没有缩进的代码全部执行一遍（模块就是一个独立的Python文件）。
# 开发人员通常会在模块下方增加一些测试代码，为了避免这些测试代码在模块被导入后执行，可以利用__name__属性。
#
# __name__属性是Python的一个内置属性，记录了一个字符串。
# 若是在当前文件，__name__ 是__main__。
print(__name__) #__main__

# 2.若是导入的文件，__name__是模块名。
# test文件导入hello模块，在test文件中打印出hello模块的__name__属性值，显示的是hello模块的模块名。
# 因此__name__ == '__main__' 就表示在当前文件中，可以在if __name__ == '__main__':条件下写入测试代码，如此可以避免测试代码在模块被导入后执行。

# 在使用命令行运行hello模块的时候，py解释器将特殊变量__name__变为__main__
# 如果在其他地方导入该hello模块时，if判断将失败
# 因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试,测试模块内的方法

