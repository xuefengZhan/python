# todo 定义一个函数要使用def语句
#  依次写出函数名、括号、括号中的参数和冒号:
#  然后，在缩进块中编写函数体
#  函数的返回值用return语句返回

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


#todo 空函数
#如果想定义一个什么事也不做的空函数，可以用pass语句：
def nop():
    pass

#todo 返回多值的函数
# 返回多个值其实是返回一个tuple对象
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
# 可以用单值接收也可以用相应的多个值接收
r = move(100, 100, 60, math.pi / 6)
x, y = move(100, 100, 60, math.pi / 6)