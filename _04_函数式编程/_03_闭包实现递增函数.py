# todo 闭包实现递增函数
# todo 方法1： 将一个迭代器作为自由变量封装到闭包函数中，在调用闭包函数的时候，每次都是迭代
def createCounter():
    def f():
        n=0
        while True:
            n=n+1
            yield n
    sun = f()
    def counter():
        return next(sun)
    return counter
ca= createCounter()
print(ca()) #1
print(ca()) #2

#todo 错误写法
def createCounter():
    i = 0
    def counter():
        i = i + 1
        return i
    return counter
# 在闭包中不能修改外部作用域的局部变量，
# 所以在外层函数设置局部变量，到内层函数再赋值返回会抛出错误： UnboundLocalError: local variable 'n' referenced before assignment

#todo 正确写法2:  由于外部变量不能在内部函数中做修改，指的是修改其值，这里用数组，这样不改地址，改变地址存的东西
def createCounter():
    i = [0]

    def counter():
        i[0] += 1
        return i[0]
    return counter