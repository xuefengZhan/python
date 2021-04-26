#todo 1.变量可以指向函数
x = abs(-10)
print(x)

f=abs
print(f(-10))
# 结论：函数本身也可以赋值给变量，即：变量可以指向函数。
# 可以通过变量来调用函数

# todo 2.函数名也是变量
# 函数名可以看成变量，它指向一个可以计算的函数！

# todo 3.函数当做参数使用
def add(x, y, f):
    return f(x) + f(y)

print(add(-1, -2, abs)) #3

# todo 4.函数做返回值
#  在函数中定义函数，并当做返回值返回
#  作用：调用外部函数的时候，不直接返回结果,而是返回一个函数
#  此函数封装了相关的参数和变量，只有调用这个函数的时候，才能够获得结果
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
# todo 4.1闭包概念
#  内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
#  当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，
#  这种称为“闭包（Closure）”的程序结构拥有极大的威力

# todo 4.2 每次调用都会返回一个新的函数对象，即使传入相同的参数


