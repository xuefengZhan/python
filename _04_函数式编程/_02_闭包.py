# todo 在计算机科学中，闭包（英语：Closure），是引用了自由变量的函数。
#  这个被引用的自由变量将和这个函数一同存在，即使已经离开了创造它的环境也不例外。
#  闭包的每个实例引用的自由变量互不干扰。
#  一个闭包实例对其自由变量的修改会被传递到下一次该闭包实例的调用。
#  (简而言之就是自由变量相当于自己的内部变量，闭包实例相当于一个对象，那么自由变量就变成了属性)
#  一个函数定义中引用了函数外定义的变量，并且该函数可以在其定义环境外被执行
#  函数内定义的变量包括： 参数 和 函数内部的变量   函数外定义的变量就是在函数外部的变量
#  函数定义的环境：就是这个函数定义所在的block


#todo 1.例1
def outer_func():
     loc_list = []
     def inner_func(name):
         loc_list.append(len(loc_list) + 1)
         print ('%s loc_list = %s' %(name, loc_list))
     return inner_func

c1 = outer_func()
print(c1('zxf'))
print(c1('zxf2'))
print(c1('zxf3'))

c2 = outer_func()
print(c2('gg'))
print(c2('gg'))
print(c2('gg'))


#todo 2.闭包陷阱
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs
# count()返回的并不是一个闭包函数，而是一个包含三个闭包函数的一个list。
fs1=count()[0]
fs2=count()[1]
fs3=count()[2]
print(fs1())  #9
print(fs2())  #9
print(fs3())  #9
# todo 但是注意：所有闭包函数均引用父函数中定义的同一个自由变量i
#  但这里的问题是为什么for循环中的变量变化会影响到所有的闭包函数？
#  尤其是我们上面刚刚介绍的例子中明明说明了同一闭包的不同实例中引用的自由变量互相没有影响的。而且这个观点也绝对的正确。
#  ##那么问题到底出在哪里？应该怎样正确的分析这个错误的根源。
#  其实问题的关键就在于在返回闭包列表fs之前for循环的变量的值已经发生改变了，
#  而且这个改变会影响到所有引用它的内部定义的函数。因为在函数count()返回前其内部定义的函数并不是闭包函数，只是一个内部定义的函数。
#  也就是说一个函数只有在被返回的时刻，被返回的时刻才会被打包成一个闭包。

# todo 例2
def my_func2(*args):
    fs=[]
    j=0
    for i in range(3):
        def func():
            return j*j
        fs.append(func)
    j=4
    return fs
m1=my_func2()[0]
m2=my_func2()[1]
m3=my_func2()[2]
print(m1())  #16
print(m2())  #16
print(m3())  #16
# todo 验证了：在内部定义的函数func实际执行前，对局部变量j的任何改变均会影响到函数func的运行结果。



#todo  修改  注意区别： 这里list添加的不是函数变量，而是函数调用；这样，在函数添加进去的时候，函数就调用了，添加进去的是g
def count1():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))   # f(i)立刻被执行，因此i的当前值被传入f()   这个相当于没有闭包，而是直接讲函数f(i)的执行结果放进了list中
    return fs
fw1=count1()[0]
fw2=count1()[1]
fw3=count1()[2]
print(fw1())  #1
print(fw2())  #4
print(fw3())  #9

